# import winsound
# import time

# duration = 30  # total seconds
# start_time = time.time()

# freq = 500  # starting frequency

# while time.time() - start_time < duration:
#     winsound.Beep(freq, 100)  # short beep (100 ms)
#     time.sleep(0.1)           # small gap like ticking
    
#     freq += 20                # increase pitch gradually
    
#     if freq > 2000:           # reset if too high
#         freq = 500

# import winsound
# import time

# duration = 5
# start = time.time()

# freq = 600  # starting pitch
# delay = 0.5 # starting gap between ticks

# while time.time() - start < duration:
#     winsound.Beep(freq, 80)   # short tick sound
#     time.sleep(delay)
    
#     # make it more intense
#     freq += 100        # pitch increases
#     delay *= 0.7       # ticks get faster

# final "explosion" sound 💥
# winsound.Beep(2000, 800)


# import winsound
# import time

# # 🔴 1. Pre-explosion tension (fast rising ticks)
# for i in range(15):
#     winsound.Beep(600 + i*80, 40)
#     time.sleep(0.03)

# # 💥 2. Explosion burst (multiple layered tones)
# for freq in [800, 1200, 1600, 2000]:
#     winsound.Beep(freq, 100)

# # 🔊 3. Deep rumble effect (low frequency pulses)
# for i in range(5):
#     winsound.Beep(200 - i*20, 150)

# # 🌫️ 4. Fading echo (descending tones)
# for i in range(6):
#     winsound.Beep(1000 - i*120, 80)
#     time.sleep(0.05)

# import winsound
# import time

# for i in range(20):  # number of "tu"
#     winsound.Beep(1000, 200)  # short sharp sound
#     time.sleep(0.8)           # gap between sounds

# import winsound
# import time

# delay = 0.9   # start slow
# freq = 900    # deep "bong" tone

# for i in range(8):
#     winsound.Beep(freq, 300)  # longer sound → "bong"
#     time.sleep(delay)
    
#     delay *= 0.001   # faster each time
#     freq += 10     # slightly rising pitch

# # final intense warning 🔴
# for _ in range(3):
#     winsound.Beep(1000, 150)
#     time.sleep(0.5)