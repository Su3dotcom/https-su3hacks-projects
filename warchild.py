#!/usr/bin/python3
import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import json
import subprocess

Builder.load_string("""

<Test2>:
    GridLayout:
        cols:1

        GridLayout:
            rows:1
            Label:
                text:'LogoSpace'
        GridLayout:
            rows:1
            TestForTabbedPanel:
                id: tp

<CustomWidthTabb@TabbedPanelItem>
    width: self.texture_size[0]
    padding: 10, 0
    size_hint_x: None

<TestForTabbedPanel>:
    size_hint: 1,1
    do_default_tab: False
    tab_width: None

    CustomWidthTabb:
        text: "Proxy"
        Label:
            text: 'Proxy tab results area'
            on_press: root.manager.current = 'proxy.py'

    CustomWidthTabb:
        text: "Spider"
        Label:
            text: 'Spider tab results area'
            on_press: root.manager.current = 'spidering.py'

    CustomWidthTabb:
        text: "Sniffer"     
        Label:
            text: 'Sniffer tab results area'
            on_press: root.manager.current = 'sniffer.py'

    CustomWidthTabb:
        text: "VulnScanner"   
        Label:
            text: 'Scanner tab results area'
            on_press: root.manager.current = 'Vulner_scanner.py'

    CustomWidthTabb:
        text: "PortScanner"   
        Label:
            text: 'Fifth tab results area'
            on_press: root.manager.current = 'Port-scanner.py'

    CustomWidthTabb:
        text: "Repeater"   
        Label:
            text: 'sixth tab results area'
            on_press: root.manager.current = 'http-repeater.py'

    CustomWidthTabb:
        text: "Arper"   
        Label:
            text: 'seventh tab content area'

    CustomWidthTabb:
        text: "Fingerprint"   
        Label:
            text: 'eighth tab content area'
            on_press: root.manager.current = 'Fingerprint.py'

    CustomWidthTabb:
        text: "AndroNeedle"   
        Label:
            text: 'nineth tab content area'

    CustomWidthTabb:
        text: "Decoder"   
        Label:
            text: 'tenth tab content area'

""")
Builder.load_string("""
<Test3>:
    GridLayout:
        cols:1
        size: root.width, root.height
        TestForProxy:
            id: tfp

        <TestForProxy>:
        GridLayout:
            cols:2

            Label:
                text: "Enter target host-ip: "

            TextInput:
                multinline:False

            Label:
                text: "Enter port: "

            TextInput:
                multiline:False

        Button:
            text:"Connect"
            on_press: app.btn()
""")

class Test2(Screen):
    def __init__(self, *args, **kwargs):
        super(Test2,proxy, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.ids.tp.on_tab_width, 0.1)

class TestForTabbedPanel(TabbedPanel):

    class Test3(Screen):
        class TestForProxy(ScreenManager):

        
            class SecreteServiceApp(App):
                def build(self):
                    return Test2()

if __name__ == '__main__':
    SecreteServiceApp().run()
