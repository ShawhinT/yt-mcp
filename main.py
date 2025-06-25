from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi
import csv
import re

# Create an MCP server
mcp = FastMCP("yt-shaw")

# Create prompts
@mcp.prompt()
def create_chapters_instructions() -> str:
    """Instructions for creating YouTube video chapters from a transcript."""
    with open("prompts/create_chapters.md", "r") as file:
        return file.read()

@mcp.prompt()
def write_blog_instructions() -> str:
    """Instructions for writing a blog post based on a YouTube video transcript."""
    with open("prompts/write_blog.md", "r") as file:
        return file.read()

# Create resource
@mcp.resource("yt-library://")
def yt_library() -> str:
    """Return all the videos from Shaw Talebi's YouTube channel on AI and entrepreneurship as a Markdown table"""
    
    with open("resources/videos.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        return "No data available."

    header = "| " + " | ".join(rows[0]) + " |"
    separator = "| " + " | ".join(["---"] * len(rows[0])) + " |"
    body = "\n".join(["| " + " | ".join(row) + " |" for row in rows[1:]])

    markdown_table = "\n".join([header, separator, body])
    return markdown_table

# Create tool
@mcp.tool()
async def fetch_youtube_transcript(url: str) -> str:
    """
    Extract transcript with timestamps from a YouTube video URL and format it for LLM consumption
    
    Args:
        url (str): YouTube video URL
        
    Returns:
        str: Formatted transcript with timestamps, where each entry is on a new line
             in the format: "[MM:SS] Text"
    """
    # Extract video ID from URL
    video_id_pattern = r'(?:v=|\\/)([0-9A-Za-z_-]{11}).*'
    video_id_match = re.search(video_id_pattern, url)
    
    if not video_id_match:
        raise ValueError("Invalid YouTube URL")
    
    video_id = video_id_match.group(1)
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format each entry with timestamp and text
        formatted_entries = []
        for entry in transcript:
            # Convert seconds to MM:SS format
            minutes = int(entry['start'] // 60)
            seconds = int(entry['start'] % 60)
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            
            formatted_entry = f"{timestamp} {entry['text']}"
            formatted_entries.append(formatted_entry)
        
        # Join all entries with newlines
        return "\\n".join(formatted_entries)
    
    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")

if __name__ == "__main__":
    mcp.run(transport='stdio')
