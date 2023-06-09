# Unitum

Unitum is a Discord bot designed to foster collaboration and learning among junior developers through code reviews. It aims to break down barriers and provide a platform for junior developers to share their projects and receive constructive feedback from their peers.


## Features

**- Code Review Requests:**
 Users can request code reviews by using the !request command in the designated "code-review" channel. They need to provide the programming language and a link to their GitHub repository.

**- Language-specific Channels:**
 The bot sends a message to the corresponding language channel, notifying users about a code review request in their language. This helps in organizing and streamlining the code review process. 

**- Reviewer Feedback:**
 Reviewers can react to the code review request message with a checkmark emoji and provide their feedback in the message thread. This encourages active participation and engagement from the community.

**- Review Points and Milestones:**
 Users earn review points for completing code reviews. When they reach predefined milestones, the bot awards them with medals as a recognition of their contributions to the community.

**- Encouragement and Support:**
 The bot sends messages of thanks and encouragement to users who complete code reviews, motivating them to continue supporting fellow developers.


## Installation

To use the Unitum bot, you can follow these steps to invite it to your Discord server:

1. Contact the owner of the Unitum bot and request an invitation link.

2. Once you receive the invitation link, open it in your web browser.

3. You will be redirected to the Discord website and prompted to select the server where you want to add the bot.

4. Choose the desired server from the drop-down menu and click "Authorize" to grant the necessary permissions to the bot.

5. Complete any additional verification steps if prompted.

6. The Unitum bot will now be added to your server, and you can start using its features.


If you encounter any issues or have questions about the installation process, please reach out to the bot's owners.

(NOTE: The list of langauge channels and channel IDs are server specific. If you are adding this to your own server, you must update these things accordingly.)


## Usage

To request a code review, use the following command in the "code-review" channel:

*"!request language github-link"*

Replace *langaue* with the programming language of your code and *github-link* with the link to your GitHub repository.

Reviewers can react to code review requests with a checkmark emoji and provide their feedback in the message thread.


## Contributing

Contributions to Unitum are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your changes.
3. Make your modifications and add tests if necessary.
4. Commit your changes and push the branch to your forked repository.
5. Open a pull request, describing your changes and the motivation behind them.
6. Your contribution will be reviewed, and once approved, it will be merged into the main repository.


## Troubleshooting

If you encounter any issues or need assistance with Unitum, please reach out to the developers listed in the project's GitHub repository.

## Roadmap

The following features and improvements are planned for future updates of Unitum:

- Allowing users to include links from platforms other than GitHub (e.g., - CodePen, CodeSandbox).

- Implementing a database to keep track of users' reviews and milestones.
Enhancing the frontend with more visually appealing features for awards and milestones.

- Adding automated reminders for unreviewed code review requests.

## Error Handling
The "Unitum" bot includes error handling to provide a smooth experience for users. Here are a few scenarios and how they are handled:

**Command Errors:**
 If a user enters an invalid command or uses a command in the wrong context, the bot will respond with an appropriate error message, indicating the issue and providing guidance on the correct command usage.

**Invalid Language:**
 When a user requests a code review with an invalid language, the bot will respond with an error message, informing the user that the specified language is not supported. Users are encouraged to use one of the predefined languages when making a code review request.

**Missing GitHub Link:**
 If a user forgets to include a GitHub repository link when making a code review request, the bot will respond with an error message, reminding the user to provide a valid link to their code repository.

**Unhandled Exceptions:**
 In case of any unhandled exceptions occurring during the bot's execution, an error message will be logged, and the bot will attempt to continue running. The error will also be displayed in the console for debugging purposes.

These error handling mechanisms help ensure a smooth user experience and provide helpful guidance in case of issues or mistakes. If you encounter any persistent issues or have questions, please feel free to reach out for assistance.



## License

Unitum is currently not licensed. Please consult with the project maintainers regarding the usage and distribution of the code.

