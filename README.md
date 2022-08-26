## Want to Get the Last Commit time of the  repository of list of Student 

#

### So create 2 Script 1 in JavaScript Octokit and 1 in Python using Selenium

- Get the Github repository Links from Sheet to JSON using My Own Python CLI App (Create using Pandas)
- Start the Selenium to get the browser access.
- Login to Github as the repository are private and access by authorized users only.
- Loop over the repositories using selenium browser.get and the json of links
- Visit each repository and get the xpath of the history tag and datetime attributes from that.
- As json is already present add the timeStamp in each element to the json array of object and store that at last.
- Use the write/Append that data


### Tag that Looking for is

```html
relative-time
```


### Save/Append Data with Last Commit Time

```python3

        # Save the data to a json file
        file = open(f'{filename}.txt', 'a')
        file.write(str(i))
        file.close()
```

### If Want to open each Tab in new window

```python3
        # # Open in New Tab
        # browser.execute_script("window.open('')")

        # # Switch to that new tab
        # browser.switch_to.window(browser.window_handles[j])

```