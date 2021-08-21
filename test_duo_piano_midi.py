"""
test duo_piano_midi.py
"""

import unittest
from duo_piano_midi import DuoPiano
from keyread import keyread


# class TestKeyboardWait(unittest.TestCase):
#     def test_user_for_P_key_yn_false(self):
#         key = keyread("Press the P Key: And Press Enter...", yn=False)
#         self.assertEqual(key, "P")

#     def test_user_for_P_key_yn_false(self):
#         key = keyread("Press the P Key: And Press Enter...")
#         self.assertEqual(key, False)

#     def test_timeout(self):
#         key = keyread("Dont press anything for 5 seconds")
#         self.assertIsNone(key)


class TestDuoPianoMidi(unittest.TestCase):

    name = "GENERAL:GENERAL MIDI 1"

    def find_in_list(self, str, ports):
        for port in ports:
            if str in port:
                # print (port)
                return True
        return False

    def test_duo_piano_out_port_aquire(self):
        duo_piano = DuoPiano()
        self.assertEqual(duo_piano.portsout, duo_piano.aquire_out_ports())

    def test_duo_piano_in_port_aquire(self):
        duo_piano = DuoPiano()
        self.assertEqual(duo_piano.portsin, duo_piano.aquire_in_ports())

    def test_duo_piano_in_port_recognised_portsin(self):
        duo_piano = DuoPiano()

        self.assertTrue(self.find_in_list(self.name, duo_piano.portsin))

    def test_duo_piano_out_port_recognised_portsout(self):
        duo_piano = DuoPiano()

        self.assertTrue(self.find_in_list(self.name, duo_piano.portsout))

    def test_duo_piano_in_port_recognised_aquire_in(self):
        duo_piano = DuoPiano()

        self.assertTrue(self.find_in_list(self.name, duo_piano.portsin))

    def test_duo_piano_out_port_recognised_aquire_out(self):
        duo_piano = DuoPiano()
        self.assertTrue(self.find_in_list(self.name, duo_piano.portsout))
        

    def test_recognised_in_port_and_open(self):
        """
        Find one and only one (the first) DuoPiano IN MIDI port
        """
        duo_piano = DuoPiano()
        din = duo_piano.get_duo_in()
        self.assertIsInstance(din, type(duo_piano.midiin))
        


    def test_recognised_out_port_and_open(self):
        """
        Find one and only one (the first) DuoPiano OUT MIDI port
        """
        duo_piano = DuoPiano()
        dout = duo_piano.get_duo_out()
        self.assertIsInstance(dout, type(duo_piano.midiout))



class TestDuoPianoMidiOut(unittest.TestCase):
    # def test_middle_c_quiet_midi_channel_1(self):
    #     duo_piano = DuoPiano()
    #     duo_piano.strike_note(1, 60, 10, 0.25)

    #     keyread("Did You hear that Quiet note:...? (yY/nN")

    #     duo_piano.strike_note(1, 60, 100, 0.25)
    #     keyread("Did You hear that Loud Note:...? (yY/nN")

    def test_middle_c_loud_midi_channel_1(self):
        duo_piano = DuoPiano()
        dout = duo_piano.get_duo_out()
        duo_piano.strike_note(1,60,10,.25)
        self.assertTrue(keyread("Did You hear a note ...?\n"))
        print('Press a note on the keyboard')

        


if __name__ == "__main__":
    unittest.main()
