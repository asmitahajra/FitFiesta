import gradio as gr
import os

# Assuming the videos are stored in a folder named "videos" in the same directory as your script
videos_dir = "videos"

def show_video(option):
    # Map options to video filenames
    videos = {
        "Jazz": "video1.mp4",
        "Bollywood": "video1.mp4",
        "Rock": "video1.mp4",
        "Country": "video1.mp4",
        "option5": "video1.mp4",
    }

    # Check if the option exists and construct the file path
    if option in videos:
        video_path = os.path.join(videos_dir, videos[option])
        if os.path.exists(video_path):
            # Return the video file path
            return video_path
        else:
            return "The selected video does not exist."
    else:
        return "Invalid option selected. Please choose between option1, option2, option3, option4, and option5."

# Define the Gradio interface
iface = gr.Interface(fn=show_video,
                     inputs=gr.Textbox(label="Choose your soundtrack (Jazz, Bollywood, Rock, Country)"),
                     outputs=gr.Video(label="Your Workout"),
                     title="FitFiesta.AI",
                     description="Enter one of the options (Jazz, Bollywood, Rock, Country) to display a workout.")

# Launch the interface
iface.launch(share=True)
