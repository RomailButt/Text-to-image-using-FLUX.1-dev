AI Image Generator with Hugging Face API

This is a desktop application built using Python and Tkinter that generates images based on user input by querying the Hugging Face API. Users can specify a prompt and resolution for the generated image, and the application will display the resulting image. Additionally, users can download the generated image to their local machine.

Features

- Generate images based on text prompts using Hugging Face's API.
- Customizable resolution: Specify width and height for the generated images.
- Preview images directly in the application.
- Download images to your local machine in JPEG format.
- Simple and user-friendly graphical interface built with Tkinter.

Prerequisites

- Python 3.x installed on your system.
- A Hugging Face account with API access to their models (make sure you have your API token).

Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-image-generator.git
   ```

2. Install the required packages:

   Ensure you have the required dependencies listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Hugging Face API token:

   - Create a file named `token.txt` in the root of the project directory.
   - Paste your Hugging Face API token inside `token.txt`. Make sure the file contains only the token with no extra spaces or newlines.

   Example `token.txt` content:

   ```
   hf_your_api_token
   ```

Usage

1. Run the application:

   You can start the application by running the `main.py` script:

   ```bash
   python main.py
   ```

2. Enter a prompt: 
   - In the application window, type in a text description (e.g., "a cup of coffee").
   
3. Set the resolution:
   - Enter the desired width and height for the image (optional, default is 1080x1080).

4. Generate the image:
   - Click the "Generate Image" button to generate the image based on your prompt.

5. Preview and save the image:
   - Once the image is generated, it will be displayed in the app window.
   - To save the image, click the "Download Image" button, choose a location, and save the file.

Example

- Prompt: "A beautiful sunset over a mountain."
- Resolution: 512x512

The application will query the Hugging Face API to generate an image based on the description and display it in the UI.

Project Structure

```
.
├── main.py              # Main application code
├── requirements.txt     # List of dependencies
├── token.txt            # Hugging Face API token (not included in repository)
```

Requirements

- requests: For making API requests to Hugging Face.
- Pillow: For handling image processing and display in the application.
  
These are listed in the `requirements.txt` and can be installed via pip.
