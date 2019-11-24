import math, wave, array
duration = 1 # seconds
freq = 440 # of cycles per second (Hz) (frequency of the sine waves)
volume = 100 # percent
 # signed short integer (-32768 to 32767) data
sampleRate = 44100 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
numSamples = sampleRate * duration
for i in range(13):
    f = freq * math.pow(2,(-9+i)/12)
    data = array.array('h')
    for j in range(numSamples):
        
        numSamplesPerCyc = int(sampleRate / f)
        sample = 32767 * float(volume) / 100
        sample *= math.sin(math.pi * 2 * (j % numSamplesPerCyc) / numSamplesPerCyc)
        data.append(int(sample))
    f = wave.open('SineWave_' + str(round(f,2)) + 'Hz.wav', 'w')
    f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
    f.writeframes(data.tostring())
    f.close()