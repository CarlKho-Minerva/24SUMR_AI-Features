# Edgur Features Repository

This repository stores various features developed for Edgur, aimed at enhancing user experience and functionality.

### 1. Recommender Algorithm

The recommender algorithm utilizes Pandas Chroma DB and a uniform probability approach to recommend videos based on user interests. Here's how it works:

- **Initialization:** The algorithm initializes a queue for user interests, which includes topics ranging from a minimum of four to a maximum of eight.
  
- **Topic Weight Distribution:** Topic weights are distributed among each other to ensure each topic has its space in the partition.
  
- **Recommendation Generation:** Using a random number generator (`random.randint`), the algorithm selects a video based on the generated number.

- **Interaction Tracking:** Upon user interaction with the recommended video, actions such as sharing and looping are observed. If a new tag is encountered, it's added to the user's interest dictionary.

- **Queue Management:** Videos are cached in advance to ensure they are readily available when users scroll rapidly, preventing loss from the queue.

- **Chroma DB Integration:** Chroma DB handles the vector storage part, utilizing OpenAI's embedding model (specifically OpenAI Text Embedding 3 Small) to convert words into vectors. This integration ensures that the algorithm returns the most relevant video given a specific tag while skipping videos already watched using a `watched_videos` dictionary.

### 2. AI Search

AI Search enhances traditional search functionalities by offering custom playlists or mini video courses based on existing videos in the database. Here's how it functions:

- **Query Processing:** Using POM engineering, the algorithm extracts key details from user queries to generate a curriculum of potential video titles or beginner test cues.

- **Chroma DB Utilization:** Each curriculum bullet is processed through Chroma DB to identify the most relevant video based on vector embeddings, ensuring precise content retrieval.

### 3. AI Quiz Generation

The AI Quiz feature dynamically generates multiple-choice questions from video transcripts, offering an interactive learning experience. Here's a breakdown:

- **Question Generation:** Utilizing OpenAI's API, the feature creates quiz questions directly from the video content.

- **Answer Formatting:** The generated questions include four possible answers, with one correct answer and three incorrect answers formatted as '~ Answer 1 ~ Answer 2 ~ Answer 3 ~ Answer 4'.

- **Answer Randomization:** Answers are shuffled to ensure a randomized order, enhancing user engagement and learning retention.

### 4. AI Summary on Timeout

This feature provides concise summaries of videos based on user session duration, offering quick insights into watched content. Key features include:

- **Automatic Summary Generation:** Summaries are pre-generated upon video upload, enabling efficient lookup using hash maps or dictionary operations during user sessions.

### 5. Whisper on the Web

Whisper on the Web introduces a microphone button for text input, enhancing user interaction with question-and-answer cards and search functionalities. It facilitates user engagement by allowing voice-based input for searches.

### 6. Revenue Calculation for Stripe Payouts

This feature calculates revenue distributions for Stripe Payouts API via Stripe Connect -> content creators based on Edgur's monthly revenue, inspired by models like Spotify's stream shares. It integrates business operations with revenue tracking and vendor payouts, ensuring transparent and efficient financial management.

