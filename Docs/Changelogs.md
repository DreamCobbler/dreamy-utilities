# 1.2.0

**Interface:**

- Added the *ReadString* and *ReadPassword* methods.

**Web:**

- Removed the *DownloadPage* and *DownloadSoup* functions.

**WebSession:**

- Implemented the *WebSession* class.

# 1.1.0

**Filesystem:**

- Improved exception handling in the *ReadTextFile* and *WriteTextFile* functions.

**Text:**

- Added the *FindFirstMatch* function.

- Text decoding error are now ignored in the *Stringify* function.
- The *Stringify* function now can use the provided encoding to decode the string.
- Improved *PrettifyTitle*.

**Web:**

- Added the option to customize the user-agent in the *DownloadPage* and the *DownloadSoup* functions.
- Added the option to customize the text encoding in the *DownloadPage* function.

# 1.0.0

The first release.