import pygame
import cv2
from moviepy.editor import VideoFileClip
import threading
def StartVideo():
    WIDTH, HEIGHT = 1000, 600
    video_path = "vid/startVideo.mp4"

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    def play_audio():
        clip = VideoFileClip(video_path)
        clip.audio.preview()

    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    cap = cv2.VideoCapture(video_path)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ret, frame = cap.read()
        if not ret:
            return

        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = pygame.surfarray.make_surface(frame)
        frame = pygame.transform.rotate(frame, -90)
        frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (0, 0))
        pygame.display.update()
        clock.tick(30)

    cap.release()
    pygame.quit()
