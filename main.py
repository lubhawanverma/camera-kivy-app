from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.logger import Logger
import os

class CameraApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title label
        title = Label(
            text='Camera On/Off App',
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True
        )
        layout.add_widget(title)
        
        # Camera widget
        self.camera = Camera(
            play=False,  # Start with camera off
            resolution=(640, 480),
            size_hint=(1, 0.7)
        )
        layout.add_widget(self.camera)
        
        # Button layout
        button_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.2),
            spacing=10
        )
        
        # Camera on/off button
        self.toggle_button = Button(
            text='Turn Camera ON',
            font_size='16sp',
            background_color=(0.2, 0.8, 0.2, 1)  # Green color
        )
        self.toggle_button.bind(on_press=self.toggle_camera)
        button_layout.add_widget(self.toggle_button)
        
        # Capture button
        capture_button = Button(
            text='Capture Photo',
            font_size='16sp',
            background_color=(0.2, 0.2, 0.8, 1)  # Blue color
        )
        capture_button.bind(on_press=self.capture_photo)
        button_layout.add_widget(capture_button)
        
        layout.add_widget(button_layout)
        
        # Status label
        self.status_label = Label(
            text='Camera is OFF',
            size_hint=(1, 0.1),
            font_size='14sp'
        )
        layout.add_widget(self.status_label)
        
        return layout
    
    def toggle_camera(self, instance):
        """Toggle camera on/off"""
        if self.camera.play:
            # Turn camera off
            self.camera.play = False
            self.toggle_button.text = 'Turn Camera ON'
            self.toggle_button.background_color = (0.2, 0.8, 0.2, 1)  # Green
            self.status_label.text = 'Camera is OFF'
            Logger.info('Camera: Camera turned OFF')
        else:
            # Turn camera on
            self.camera.play = True
            self.toggle_button.text = 'Turn Camera OFF'
            self.toggle_button.background_color = (0.8, 0.2, 0.2, 1)  # Red
            self.status_label.text = 'Camera is ON'
            Logger.info('Camera: Camera turned ON')
    
    def capture_photo(self, instance):
        """Capture a photo from the camera"""
        if self.camera.play:
            # Create pictures directory if it doesn't exist
            pictures_dir = '/storage/emulated/0/Pictures/CameraApp'
            if not os.path.exists(pictures_dir):
                try:
                    os.makedirs(pictures_dir)
                except:
                    pictures_dir = '/sdcard/Pictures/CameraApp'
                    try:
                        os.makedirs(pictures_dir)
                    except:
                        pictures_dir = '.'  # Fallback to current directory
            
            # Generate filename with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{pictures_dir}/photo_{timestamp}.png"
            
            # Export camera texture to file
            self.camera.export_to_png(filename)
            self.status_label.text = f'Photo saved: photo_{timestamp}.png'
            Logger.info(f'Camera: Photo saved to {filename}')
        else:
            self.status_label.text = 'Turn camera ON first to capture photo'
    
    def on_pause(self):
        """Handle app pause (turn off camera to save battery)"""
        if self.camera.play:
            self.camera.play = False
        return True
    
    def on_resume(self):
        """Handle app resume"""
        pass

if __name__ == '__main__':
    CameraApp().run()
