from time import sleep
from picamera import PiCamera


def main():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')


if __name__ == "__main__":
    main()
