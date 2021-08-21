"""
Ruggedising the duo piano

Wake Up:
    detect duopiano connection
    send midi message ( which?) to
    Duo-piano
    while port:
        # Keep awake?
        send keep_alive
       

"""

DUO_PIANO_STRING = "GENERAL:GENERAL MIDI 1"

import time
import rtmidi


class DuoPiano:
    def __init__(self):
        self.midiout = rtmidi.MidiOut()
        self.midiin = rtmidi.MidiIn()

        self.portsin = self.aquire_in_ports()
        self.portsout = self.aquire_out_ports()

    def aquire_in_ports(self):
        return self.midiout.get_ports()

    def aquire_out_ports(self):
        return self.midiout.get_ports()

    def get_duo_out(self):
        """Find the term GENERAL MIDI
        and identify list index

        """

        res_dict = {}

        for count, item in enumerate(self.midiout.get_ports()):
            if DUO_PIANO_STRING in item:
                return self.midiout.open_port(count)

        return None

    def get_duo_in(self):
        """Find the term GENERAL MIDI
        and return open port

        """
        res_dict = {}

        for count, item in enumerate(self.midiin.get_ports()):
            # print(count, item)

            if DUO_PIANO_STRING in item:
                return self.midiin.open_port(count)

        return None

    def strike_note(self, channel, note, velocity, duration):

        """1, 60, 10,.25)"""
        with self.midiout:
            note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
            note_off = [0x80, 60, 0]
            self.midiout.send_message(note_on)
            time.sleep(0.5)
            self.midiout.send_message(note_off)
            time.sleep(0.1)

        del self.midiout


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

with midiout:
    note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)
    time.sleep(0.1)

del midiout
