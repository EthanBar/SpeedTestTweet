import pyspeedtest
import twitter

'''
Simple python script that uses Ookla speedtest
servers. Then if speeds are significantly below
normal, tweets using Python Twitter
'''


def run():
    print("Twitter init...")
    api = twitter.Api("y4zqS0roH2NiA153E9a3ai3Zn", "yOdBoQWJ1o58QOCRKuRy5510kdsTRwUiPYhusIsnnJVWAZjiSZ"
                      , "879429529508491264-YSiGGrH3ZqzAW1H9xWix7SM5eV5qP25",
                      "eNDEbV88QAJSX3ZizQA5YbPmpOiZcqztg9JdZshdgRMhX")

    print("Running speed test..")
    st = pyspeedtest.SpeedTest()

    # Divide by a million as the values from pyspeedtest are in bytes (I think...)
    down_speed = st.download() / 1000000
    up_speed= st.upload() / 1000000

    if down_speed < 30 or up_speed < 1.5:
        print("Bad speeds, tweeting")
        message = "@bendbroadband I'm paying for 50down/3up, why is my speed " + str(round(down_speed, 2)) +\
                  "down/" + str(round(up_speed, 2)) + "up?"
        print(message)
        api.PostUpdate(message)
    else:
        print("Normal Speed found, message would be: ")
        print("@bendbroadband I'm paying for 50down/3up, why is my speed " + str(round(down_speed, 2)) + \
                  "down/" + str(round(up_speed, 2)) + "up?")

if __name__ == "__main__":
    run()
    print("Speed test completed")
