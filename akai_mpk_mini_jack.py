# Device handler for AKAI_MPK_MINI
import jack
import struct
import time
client = jack.Client("test")

messages = [] # Holds list of pending MIDI messages

# Jack process callback that does all the work - don't put slow or blocking stuff in here
@client.set_process_callback
def process(frames):
    global messages
    outport.clear_buffer() # Need to clear the output buffer each cycle otherwise the same messages get resent
    # Iterate incoming MIDI data
    for offset, indata in inport.incoming_midi_events():
        if len(indata) == 3:
            status, val1, val2= struct.unpack('3B', indata)
    # Iterate through outgoing message queue, sending each pending message at end of frame (may work with 0 to send at start of frame but didn't once hence I put frames-1 in)
    for message in messages:
        outport.write_midi_event(frames-1, message)
    messages = [] # Let's hope they all went!

# Create MIDI input and output ports for this jack client    
outport = client.midi_outports.register('output')
inport = client.midi_inports.register('input')
client.activate()

#client.connect(outport, "name of destination jack MIDI port")

# To send MIDI append (status, val1, val2) to messages[], e.g. to 
# send note-on for middle C with velocity 100: messages.append((0x90, 60, 100))

if __name__ == '__main__':
    for i in range(128):
        for j in range(128):
            messages.append((0x80, i, j ))
            print (messages)
            time.sleep(.1)