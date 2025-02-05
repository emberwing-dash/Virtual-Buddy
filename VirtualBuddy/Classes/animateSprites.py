import pygame

class SpriteSheetAnimation:
    def __init__(self, sprite_sheet_image, frame_width, frame_height, num_frames, frame_rate):
        self.sprite_sheet = pygame.image.load(sprite_sheet_image).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.num_frames = num_frames
        self.frame_rate = frame_rate

        # List to store the individual frames
        self.frames = self.extract_frames()

        # Initial animation state
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

    def extract_frames(self):
        """ Extract individual frames from the sprite sheet. """
        frames = []
        sheet_width, sheet_height = self.sprite_sheet.get_size()

        for i in range(self.num_frames):
            # Calculate the x, y position of each frame in the sprite sheet
            x = (i % (sheet_width // self.frame_width)) * self.frame_width
            y = (i // (sheet_width // self.frame_width)) * self.frame_height

            # Create a surface for each frame
            frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
            frames.append(frame)

        return frames

    def update(self):
        """ Update the current frame for animation. """
        now = pygame.time.get_ticks()

        # Only update frame if enough time has passed (based on frame rate)
        if now - self.last_update > 1000 / self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % self.num_frames

    def draw(self, surface, x, y):
        """ Draw the current frame to the surface at position (x, y). """
        surface.blit(self.frames[self.current_frame], (x, y))
