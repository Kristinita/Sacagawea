# -*- coding: utf-8 -*-
# @Author: Keith Hall
# @Date: 2017-04-24 06:43:14
# @Last Modified time: 2017-04-27 14:22:22
"""Sacagawea countdown timer.

Sublime Text timer for “What? Where? When?” and “Brain Ring” games. Keith Hall
timer based on http://bit.ly/2q7C1UA timer. Full description see in
http://Kristinita.ru/Sublime-Text/Sacagawea page.
"""
import os
import subprocess

import sublime
import sublime_plugin
# [H2] Regular (03) ASCII Decorator font
"""

 #####
#     #
#         ######   #####    ######   ######   ######  #     #   #####    ######
 #####   #     #  #        #     #  #     #  #     #  #  #  #  #     #  #     #
      #  #     #  #        #     #  #     #  #     #  #  #  #  #######  #     #
#     #  #    ##  #        #    ##  #     #  #    ##  #  #  #  #        #    ##
 #####    #### #   #####    #### #   ######   #### #   ## ##    #####    #### #
                                          #
                                     #####
"""
# Get plugin path
# http://stackoverflow.com/a/3430395/5951529
# Relative path doesn't work
# http://stackoverflow.com/posts/comments/74265277
ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))


# Global variables
# Default or custom sounds
SETTINGS = sublime.load_settings(
    "Sacagawea.sublime-settings")
BEGIN_PATH = SETTINGS.get(
    "custom_begin_sound_path")
TEN_SECONDS_PATH = SETTINGS.get(
    "custom_ten_seconds_sound_path")
END_PATH = SETTINGS.get(
    "custom_end_sound_path")

# https://www.soundjay.com/beep-sounds-1.html
if BEGIN_PATH == "default":
    BEGIN_SOUND = [
        "mpg123",
        "-q", ABSOLUTE_PATH + os.sep + "sounds" + os.sep + "beep-01a.mp3"]
else:
    BEGIN_SOUND = [
        "mpg123",
        "-q", BEGIN_PATH]

# https://www.soundjay.com/beep-sounds-1.html
if TEN_SECONDS_PATH == "default":
    TEN_SECONDS_SOUND = [
        "mpg123",
        "-q", ABSOLUTE_PATH + os.sep + "sounds" + os.sep + "beep-09.mp3"]
else:
    BEGIN_SOUND = [
        "mpg123",
        "-q", TEN_SECONDS_PATH]

# https://www.soundjay.com/censor-beep-sound-effect.html
if END_PATH == "default":
    END_SOUND = [
        "mpg123",
        "-q", ABSOLUTE_PATH + os.sep + "sounds" + os.sep + "censor-beep-7.mp3"]
else:
    END_SOUND = [
        "mpg123",
        "-q", END_PATH]


class SacagaweaChgkCommand(sublime_plugin.TextCommand):
    """sacagawea_chgk_command.

    Command for run standard “What? Where? When?” timer.

    Extends:
        sublime_plugin.TextCommand
    """

    def run(self, edit, seconds=60):
        """Run 60 seconds timer.

        Countdown 60 seconds timer.

        Arguments:
            edit {str} -- view for editing.

        Keyword Arguments:
            seconds {number} -- number of seconds, from which the countdown
            begins. (default: {60})
        """
        self.print_seconds(sublime.active_window().new_file(), seconds)

    def print_seconds(self, view, seconds):
        """print_seconds function.

        Keith Hall timer based on Python timer.

        Arguments:
            view {str} -- view for editing.
            seconds {int} -- second, in which run actions.
        """
        # Break if current view is not valid.
        # For example, if you close current view.
        # http://bit.ly/2q7B1Qr
        if not view.is_valid():
            return
        text = ''
        if seconds >= 0:
            text = str(seconds)
            if seconds == 60:
                # Bruce Buffer phrase
                # https://www.youtube.com/watch?v=y4sdZN7blfE
                text = 'Here we go!'
                # Run shell command,
                # http://bit.ly/2q6fOUi
                subprocess.Popen(BEGIN_SOUND, shell=True)
            sublime.set_timeout_async(
                lambda: self.print_seconds(
                    view, seconds - 1), 1000)
            if seconds == 10:
                text += ' seconds. Select a version!'
                subprocess.Popen(TEN_SECONDS_SOUND, shell=True)
            if seconds == 0:
                subprocess.Popen(END_SOUND, shell=True)
                text = 'Time over!'
                # Timeout before run command force_quit;
                # set_timeout_async method
                # https://www.sublimetext.com/docs/3/api_reference.html#sublime
                # http://stackoverflow.com/posts/comments/74219257
                sublime.set_timeout_async(
                    lambda: view.window().run_command('force_quit'), 5000)

        # Use command from ScrollAlternative package:
        # https://packagecontrol.io/packages/ScrollAlternative
        # Don't work “or” operator:
        # http://stackoverflow.com/a/15112149/5951529
        if seconds in {40, 20}:
            view.run_command("scroll_lines_enhanced", {"amount": 20})
        if seconds == 10:
            view.run_command("scroll_lines_enhanced", {"amount": 10})
        # Append command for print text to new view, not to console:
        # http://stackoverflow.com/a/43582267/5951529
        view.run_command(
            'append', {
                'characters': text + '\n'})
        # Remove carriage in new view
        # https://www.sublimetext.com/docs/3/api_reference.html#sublime.Selection
        view.selection.clear()


class SacagaweaBlitzCommand(sublime_plugin.TextCommand):
    """sacagawea_blitz_command.

    Command — run timer for blitz/supeblitz in “What? Where? When?” and Brain
    Ring.

    Extends:
        sublime_plugin.TextCommand
    """

    def run(self, edit, seconds=20):
        """Run 20 seconds timer.

        Countdown 20 seconds timer.

        Arguments:
            edit {str} -- view for editing.

        Keyword Arguments:
            seconds {number} -- number of seconds, from which the countdown
            begins. (default: {20})
        """
        self.print_seconds(sublime.active_window().new_file(), seconds)

    def print_seconds(self, view, seconds):
        """print_seconds function.

        Same descriptioin as for SacagaweaChgkCommand class.

        Arguments:
            view {str} -- view for editing.
            seconds {int} -- second, in which run actions.
        """
        if not view.is_valid():
            return
        text = ''
        if seconds >= 0:
            text = str(seconds)
            if seconds == 20:
                text = 'Here we go!'
                subprocess.Popen(BEGIN_SOUND, shell=True)
            sublime.set_timeout_async(
                lambda: self.print_seconds(
                    view, seconds - 1), 1000)
            if seconds == 10:
                text += ' seconds. Select a version!'
                subprocess.Popen(TEN_SECONDS_SOUND, shell=True)
            if seconds == 0:
                subprocess.Popen(END_SOUND, shell=True)
                text = 'Time over!'
                sublime.set_timeout_async(
                    lambda: view.window().run_command('force_quit'), 5000)

        if seconds == 10:
            view.run_command("scroll_lines_enhanced", {"amount": 20})
        view.run_command(
            'append', {
                'characters': text + '\n'})
        view.selection.clear()
