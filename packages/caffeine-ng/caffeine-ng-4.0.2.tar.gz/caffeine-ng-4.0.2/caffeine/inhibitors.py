# Copyright (c) 2015-2022 Hugo Osvaldo Barrera <hugo@barrera.io>
#
# SPDX-License-Identifier: GPL-3.0+

import logging
import os
import shutil
import threading
import time
from abc import ABC
from abc import abstractmethod

import dbus

logger = logging.getLogger(__name__)

INHIBITION_REASON = "Inhibited via libcaffeine"


class BaseInhibitor(ABC):
    running: bool

    def __init__(self):
        self.running = False

    def set(self, state: bool) -> None:
        if state:
            if not self.running:
                self.inhibit()
        else:
            if self.running:
                self.uninhibit()

    def is_screen_inhibitor(self):
        """Return True if this instance is a screen saver inhibitor.

        Inhibitor which are sleep inhibitors should return False.
        """
        return False

    @property
    @abstractmethod
    def applicable(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def inhibit(self, reason=INHIBITION_REASON) -> None:
        raise NotImplementedError()

    @abstractmethod
    def uninhibit(self) -> None:
        raise NotImplementedError()

    def __str__(self):
        return self.__class__.__name__


class GnomeInhibitor(BaseInhibitor):
    def __init__(self):
        super().__init__()
        self.bus = dbus.SessionBus()

        self.__proxy = None
        self.__cookie = None

    def inhibit(self, reason=INHIBITION_REASON) -> None:
        if not self.__proxy:
            self.__proxy = self.bus.get_object(
                "org.gnome.SessionManager",
                "/org/gnome/SessionManager",
            )
            self.__proxy = dbus.Interface(
                self.__proxy,
                dbus_interface="org.gnome.SessionManager",
            )

        self.__cookie = self.__proxy.Inhibit(
            "Caffeine",
            dbus.UInt32(0),
            INHIBITION_REASON,
            dbus.UInt32(4),
        )
        self.running = True

    def uninhibit(self) -> None:
        if self.__cookie is not None:
            self.__proxy.Uninhibit(self.__cookie)
        self.running = False

    @property
    def applicable(self) -> bool:
        return "org.gnome.SessionManager" in self.bus.list_names()


class XdgScreenSaverInhibitor(BaseInhibitor):
    def __init__(self):
        super().__init__()
        self.bus = dbus.SessionBus()

        self.__cookie = None

    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.__proxy = self.bus.get_object(
            "org.freedesktop.ScreenSaver",
            "/ScreenSaver",
        )
        self.__proxy = dbus.Interface(
            self.__proxy,
            dbus_interface="org.freedesktop.ScreenSaver",
        )
        self.__cookie = self.__proxy.Inhibit("Caffeine", INHIBITION_REASON)

        self.running = True

    def uninhibit(self) -> None:
        if self.__cookie:
            self.__proxy.UnInhibit(self.__cookie)
        self.running = False

    def is_screen_inhibitor(self):
        return True

    @property
    def applicable(self) -> bool:
        return "org.freedesktop.ScreenSaver" in self.bus.list_names()


class XdgPowerManagmentInhibitor(BaseInhibitor):
    def __init__(self):
        super().__init__()
        self.bus = dbus.SessionBus()

        self.__cookie = None

    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.__proxy = self.bus.get_object(
            "org.freedesktop.PowerManagement",
            "/org/freedesktop/PowerManagement/Inhibit",
        )
        self.__proxy = dbus.Interface(
            self.__proxy,
            dbus_interface="org.freedesktop.PowerManagement.Inhibit",
        )
        self.__cookie = self.__proxy.Inhibit("Caffeine", INHIBITION_REASON)
        self.running = True

    def uninhibit(self) -> None:
        if self.__cookie:
            self.__proxy.UnInhibit(self.__cookie)
        self.running = False

    @property
    def applicable(self) -> bool:
        return "org.freedesktop.PowerManagement" in self.bus.list_names()


class XssInhibitor(BaseInhibitor):
    class XssInhibitorThread(threading.Thread):
        keep_running = True
        daemon = True

        def run(self):
            logging.info("Running XSS inhibitor thread.")
            while self.keep_running:
                os.system("xscreensaver-command -deactivate")
                time.sleep(50)
            logging.info("XSS inhibitor thread finishing.")

    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.running = True
        self.thread = XssInhibitor.XssInhibitorThread()
        self.thread.start()

    def uninhibit(self) -> None:
        self.running = False
        self.thread.keep_running = False

    @property
    def applicable(self) -> bool:
        # TODO!
        return os.system("pgrep xscreensaver") == 0


class DpmsInhibitor(BaseInhibitor):
    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.running = True

        os.system("xset -dpms")

    def uninhibit(self) -> None:
        self.running = False

        # FIXME: Aren't we enabling it if it was never online?
        # Grep `xset q` for "DPMS is Enabled"
        os.system("xset +dpms")

    def is_screen_inhibitor(self):
        return True

    @property
    def applicable(self) -> bool:
        # TODO: Condition is incomplete
        return os.environ.get("WAYLAND_DISPLAY") is None


class XorgInhibitor(BaseInhibitor):
    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.running = True
        os.system("xset s off")

    def uninhibit(self) -> None:
        self.running = False

        # FIXME: Aren't we enabling it if it was never online?
        # Scrensaver.*\n\s+timeout:  600
        os.system("xset s on")

    @property
    def applicable(self) -> bool:
        # TODO: Condition is incomplete
        return os.environ.get("WAYLAND_DISPLAY") is None


class XautolockInhibitor(BaseInhibitor):
    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.running = True
        os.system("xautolock -disable")

    def uninhibit(self) -> None:
        self.running = False
        os.system("xautolock -enable")

    @property
    def applicable(self) -> bool:
        return os.system("pgrep xautolock") == 0


class XfceInhibitor(BaseInhibitor):
    def __init__(self):
        BaseInhibitor.__init__(self)

    def inhibit(self):
        self.running = True

        os.system(
            "xfconf-query -c xfce4-power-manager"
            "-p /xfce4-power-manager/presentation-mode -s true"
        )

    def uninhibit(self):
        self.running = False

        os.system(
            "xfconf-query -c xfce4-power-manager"
            "-p /xfce4-power-manager/presentation-mode -s false"
        )

    @property
    def applicable(self):
        # If `xfconf-query` is absent, this is not applicable.
        return shutil.which("xfconf-query") is not None


class XidlehookInhibitor(BaseInhibitor):
    def inhibit(self, reason=INHIBITION_REASON) -> None:
        self.running = True
        os.system("pkill -SIGSTOP xidlehook")

    def uninhibit(self) -> None:
        self.running = False
        os.system("pkill -SIGCONT xidlehook")

    @property
    def applicable(self) -> bool:
        return os.system("pgrep xidlehook") == 0
