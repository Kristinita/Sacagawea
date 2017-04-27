# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2017-04-27 11:39:19
# @Last Modified time: 2017-04-27 21:35:24
import os
import sublime
import sublime_plugin
import subprocess

ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))


def plugin_loaded():
    global SETTINGS, BEGIN_PATH, BEGIN_SOUND

    SETTINGS = sublime.load_settings(
        "Sacagawea.sublime-settings")
    BEGIN_PATH = SETTINGS.get(
        "custom_begin_sound_path")
    if BEGIN_PATH == "default":
        BEGIN_SOUND = [
            "mpg123",
            "-q", ABSOLUTE_PATH + os.sep + "sounds" + os.sep + "beep-01a.mp3"]
    else:
        BEGIN_SOUND = [
            "mpg123",
            "-q", BEGIN_PATH]


class LovernaStandardCommand(sublime_plugin.TextCommand):

    def run(self, edit, seconds=10):
        self.print_seconds(sublime.active_window().new_file(), seconds)

    def print_seconds(self, view, seconds):
        text = ''
        if seconds > 0:
            text = str(seconds)
            if seconds == 5:
                text += ' seconds'
                subprocess.Popen(BEGIN_SOUND, shell=True)
            sublime.set_timeout_async(
                lambda: self.print_seconds(
                    view, seconds - 1), 1000)
        else:
            text = 'Time over!'
        view.run_command(
            'append', {
                'characters': text + '\n'})
