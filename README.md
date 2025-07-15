# Reddit Persona Generator

A Python script that analyzes Reddit user profiles and generates detailed persona profiles using AI. The script extracts a user's recent posts and comments, then uses Google's Gemini AI to create a structured personality analysis.

## Features

- Extract recent Reddit posts and comments from any user profile
- Generate detailed persona analysis including age, location, profession, interests, personality traits, and writing style
- Export results as both Markdown and HTML files
- Professional formatting with direct quotes and source citations
- **Interactive HTML viewer** with Streamlit for enhanced persona visualization

## Prerequisites

Before running this script, you'll need:

1. **Python 3.7+** installed on your system
2. **Reddit API credentials** (see setup instructions below)
3. **Google Gemini API key** (for AI analysis)

## Installation

1. **Clone or download the script** to your local machine

2. **Install required Python packages:**
   ```bash
   pip install praw python-dotenv google-generativeai markdown streamlit
   ```

## Reddit API Setup

### Step 1: Create a Reddit App

1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Sign in to your Reddit account
3. Scroll down to the "Developed Applications" section
4. Click **"Create App"** or **"Create Another App"**

### Step 2: Configure Your App

Fill out the form with these details:
- **Name**: Choose any name (e.g., "Reddit Persona Generator")
- **App type**: Select **"script"**
- **Description**: Optional description of your app
- **About URL**: Leave blank or add your GitHub repo
- **Redirect URI**: Enter `http://localhost:8080` (required but not used)

### Step 3: Get Your API Credentials

After creating the app, you'll see:
- **Client ID**: The string directly under your app name (looks like: `abc123def456`)
- **Client Secret**: The longer string labeled "secret" (looks like: `xyz789abc123def456ghi789`)

## Environment Setup

### Step 1: Create a .env file

Create a file named `.env` in the same directory as your script.

### Step 2: Add your credentials

Copy and paste this template into your `.env` file, replacing the placeholder values:

```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_password_if_needed
USER_AGENT=script:RedditPersonaGen:v1.0 (by u/yourusername)
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 3: Fill in your actual values

- **REDDIT_CLIENT_ID**: Paste your client ID from the Reddit app
- **REDDIT_CLIENT_SECRET**: Paste your client secret from the Reddit app
- **REDDIT_USERNAME**: Your Reddit username (without the u/ prefix)
- **REDDIT_PASSWORD**: Your Reddit password (if using password authentication)
- **USER_AGENT**: Update with your Reddit username (e.g., `script:RedditPersonaGen:v1.0 (by u/yourname)`)
- **GEMINI_API_KEY**: Your Google Gemini API key

## Google Gemini API Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key
5. Add it to your `.env` file as `GEMINI_API_KEY`

## Usage

### Generating Personas

1. **Run the main script:**
   ```bash
   python main.py
   ```

2. **Enter a Reddit profile URL** when prompted. Examples:
   - `https://www.reddit.com/user/username`
   - `https://reddit.com/u/username`

3. **Wait for processing** - the script will:
   - Extract the user's recent posts and comments
   - Send the data to Gemini AI for analysis
   - Generate a detailed persona profile

4. **Check the output** - files will be saved in the `output/` directory:
   - `persona_username.md` - Markdown version
   - `persona_username.html` - HTML version (styled)

### Viewing HTML Personas (Interactive Viewer)

For a better viewing experience of the generated persona profiles, you can use the interactive HTML viewer:

1. **Launch the Streamlit viewer:**
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser** and navigate to the local URL (usually `http://localhost:8501`)

3. **Select a persona profile** from the dropdown menu to view any previously generated HTML profiles

4. **Enhanced viewing features:**
   - Clean, formatted HTML display
   - Clickable Reddit URLs for easy verification
   - Scrollable interface for long profiles
   - Professional styling and formatting

**Note for recruiters:** If you want to see a properly formatted HTML version of the persona profiles with enhanced readability and clickable links, simply run `streamlit run app.py` after generating personas to access the interactive viewer.

## Output Format

The generated persona includes:

- **Age**: Estimated age range with supporting evidence
- **Location**: Geographic location if mentioned
- **Profession**: Job or field of work
- **Interests & Hobbies**: Up to 5 main interests with quotes
- **Personality Traits**: Behavioral characteristics (minimum 3)
- **Writing Style**: Communication patterns and tone
- **Mental/Emotional Cues**: Psychological insights (minimum 2)

Each section includes direct quotes from the user's posts/comments and source URLs for verification.

## Important Notes

### Privacy and Ethics
- Only analyze public Reddit profiles
- Respect user privacy and Reddit's terms of service
- Use generated personas responsibly and ethically
- Consider the implications of personality analysis

### Rate Limits
- Reddit API has rate limits - avoid rapid successive requests
- The script processes up to 50 recent posts and 50 recent comments
- Large profiles may take longer to process

### Accuracy
- AI analysis is based on limited public data
- Personas are interpretations, not definitive assessments
- Results may not reflect the complete personality of a user

## Troubleshooting

### Common Issues:

1. **"Invalid credentials" error**
   - Double-check your Reddit client ID and secret
   - Ensure your .env file is in the correct directory
   - Verify your Reddit username and password

2. **"User not found" error**
   - Check the Reddit URL format
   - Ensure the username exists and is public
   - Some users may have restricted profiles

3. **Gemini API errors**
   - Verify your Gemini API key is correct
   - Check if you have API quota remaining
   - Ensure your Google Cloud project has the Gemini API enabled

4. **Missing packages**
   - Install required packages: `pip install praw python-dotenv google-generativeai markdown streamlit`

5. **Streamlit viewer issues**
   - Ensure Streamlit is installed: `pip install streamlit`
   - Check that HTML files exist in the `output/` directory
   - Verify your Gemini API key is correctly set in the .env file

## File Structure

```
your-project/
├── main.py  # Main script for generating personas
├── app.py                       # Streamlit viewer for HTML personas
├── .env                        # Environment variables (API keys)
├── output/                     # Generated persona files
│   ├── persona_username.md
│   └── persona_username.html
└── README.md
```

## License

This project is for educational and research purposes. Please use responsibly and in accordance with Reddit's API terms of service and privacy policies.

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all API credentials are correct
3. Ensure all required packages are installed
4. Check Reddit and Google API status pages for service issues
