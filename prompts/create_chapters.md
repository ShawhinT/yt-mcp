# Video Chapter Generation Instructions

## Overview
Generate meaningful chapter timestamps that help viewers navigate to specific topics within a video. Chapters should be concise, descriptive, and represent clear topic transitions.

## Step-by-Step Process

### 1. **Read Through the Entire Transcript**
- Understand the overall structure and flow
- Identify the main topics covered
- Note natural transition points between concepts

### 2. **Identify Major Topic Shifts**
Look for these indicators of new chapters:
- **Explicit transitions**: Phrases like "Let's now dive into...", "Next, we'll...", "Now let's make this concrete..."
- **Topic introductions**: "First, we'll start with...", "Another key component is..."
- **Conceptual shifts**: Moving from theory to practice, from overview to implementation
- **Structural markers**: "Step 1", "Step 2", numbered sections, bullet points being introduced

### 3. **Create Descriptive Chapter Titles**
Follow these naming conventions:
- **Keep it concise**: 1-4 words maximum (shorter is often better)
- **Use broad, conceptual terms**: Focus on main topics rather than specific details
- **Match the speaker's exact language**: Use key terms directly from the video
- **Prefer nouns over action words**: "Workflows" not "Understanding Workflows"
- **Avoid overly specific details**: "Design Patterns" not "Six Common Design Patterns"
- **Use speaker's unique terminology**: Include distinctive phrases they emphasize

### 4. **Determine Precise Timestamps**
- Use the timestamp where the new topic is **first mentioned or introduced**
- Don't wait for the topic to be fully explained
- Round to the nearest 5-second interval (0:00, 0:05, 0:10, etc.)
- Ensure logical progression (each timestamp should be later than the previous)

### 5. **Chapter Naming Patterns**

**For Conceptual Videos:**
- "Introduction" → "Intro" 
- "What is [Topic]?" → "[Topic]" (e.g., "Workflows", "LLM Workflows")
- "Design Patterns" → "Design Patterns" (use exact speaker terminology)
- "Limitations" → Use speaker's exact phrase (e.g., "LLMs Aren't a Cure-all")

**For Implementation Videos:**
- "Building [Something]" → "Example: [Something]" or just "[Something]"
- "Demonstration" → "Demo"
- "Setup" → "Setup" (keep simple)

**Key Principles:**
- **Favor the speaker's exact memorable phrases** over generic descriptions
- **Use 1-3 words when possible**, expanding only when necessary for clarity
- **Capture the speaker's tone and style** in chapter naming
- **Prioritize conceptual groupings** over granular step-by-step breakdowns

### 6. **Quality Checks**
- **Logical flow**: Each chapter should build on the previous
- **Appropriate granularity**: Aim for 5-8 chapters total for most videos
- **Speaker's conceptual boundaries**: Align with how the speaker naturally groups topics
- **Memorable phrases**: Include distinctive terminology the speaker emphasizes
- **Viewer value**: Ask "Would someone want to jump directly to this major section?"
- **Avoid over-segmentation**: Don't create chapters for every minor topic shift

## Example Application

**From the LLM workflows video transcript:**

| Timestamp | Chapter Title | Rationale |
|-----------|---------------|-----------|
| 0:00 | Intro | Standard opening, sets context |
| 0:25 | Workflows | Speaker defines workflows with examples |
| 2:57 | LLM Workflows | Major shift to incorporating LLMs |
| 5:14 | Design Patterns | Speaker's exact section heading |
| 8:06 | LLMs Aren't a Cure-all | Speaker's distinctive phrase |
| 13:12 | Example: Artificial Virtual Assistant | Concrete implementation begins |
| 24:41 | Demo | Live demonstration starts |

## Common Mistakes to Avoid
- ❌ Too many micro-chapters (every 30 seconds) - aim for major conceptual shifts
- ❌ Overly descriptive titles ("Understanding Basic Workflows")  
- ❌ Missing the speaker's distinctive phrases and terminology
- ❌ Creating chapters for minor sub-topics instead of major sections
- ❌ Generic titles when speaker uses memorable, specific language
- ❌ Over-engineering chapter names instead of using simple, direct terms

## Template Format
```
Chapter Title - Timestamp
Chapter Title - Timestamp
Chapter Title - Timestamp
```

**Example:**
```
Intro - 0:00
Workflows - 0:25
LLM Workflows - 2:57
Design Patterns - 5:14
```