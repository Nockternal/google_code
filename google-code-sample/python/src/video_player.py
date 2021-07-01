# please note this is not my cleanest and most efficient code just a rush to get as much done as possible. 
"""A video player class."""
import random
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isplaying = None
        self.video = None
        self.isPaused = False
        self.playLists = []
        self.tagList = []
        for i in self._video_library.get_all_videos():
            self.tagList.append(
                {
                    'name': i._title,
                    'video_id': i.video_id,
                    'tags': i.tags,
                    'flagged': False,
                    'flag_reason': 'Not supplied'
                }
            )


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        mylist = []
        final_list = []
        video_list = self._video_library.get_all_videos()
        for i in video_list:
            mylist.append(f"{i._title} ({i._video_id}) ["+' '.join(i.tags)+']')
        sortedVideos_list = sorted(mylist)
        final_list.append("Here's a list of all available videos:")
        for i in sortedVideos_list:
            final_list.append(i)
        print('\n'.join(map(str, final_list)))

        
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        if self.isplaying != None:
            try:
                try:
                    newvideo = self._video_library.get_video(video_id)._title

                    print(f"Stopping video: {self.isplaying}")
                    self.isplaying = self._video_library.get_video(video_id)._title
                    self.video = video_id
                    self.isPaused = False
                    print(f"Playing video: {self._video_library.get_video(video_id)._title}")
                except Exception as e:
                    print('Cannot play video: Video does not exist')
                
            except Exception as e:
                print("Cannot play video: Video does not exist")
            
        else:
            try:
                self.isplaying = self._video_library.get_video(video_id)._title
                self.video = video_id
                print(f"Playing video: {self._video_library.get_video(video_id)._title}")
            except Exception as e:
                print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.isplaying != None:
            print(f"Stopping video: {self.isplaying}")
            self.isplaying = None
            self.isPaused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        videoList = []
        """Plays a random video from the video library."""
        database_list = self._video_library.get_all_videos()
        for i in database_list:
            videoList.append(i.video_id)
        
        self.play_video(random.choice(videoList))
        

    def pause_video(self):
        
        if self.isplaying == None:
            print("Cannot pause video: No video is currently playing")
        else:
            if self.isPaused == True:
                print(f"Video already paused: {self.isplaying}")
            elif self.isPaused == False:
                self.isPaused = True
                print(f"Pausing video: {self.isplaying}")
             

        

    def continue_video(self):
        """Resumes playing the current video."""

        if self.isplaying == None:
            print("Cannot continue video: No video is currently playing")
        else:
            if self.isPaused == True:
                print(f"Continuing video: {self.isplaying}")
                self.isPaused = False
            elif self.isPaused == False:
                print(f"Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self.isplaying == None:
            print('No video is currently playing')
        
        else:
            if self.isPaused == True:
                vidTitle = self._video_library.get_video(self.video)._title
                vidId = self._video_library.get_video(self.video).video_id
                vidTags = self._video_library.get_video(self.video).tags

                print(f"Currently playing: {vidTitle} ({vidId}) ["+' '.join(vidTags) +']'+ ' - PAUSED')
            else:
                vidTitle = self._video_library.get_video(self.video)._title
                vidId = self._video_library.get_video(self.video).video_id
                vidTags = self._video_library.get_video(self.video).tags

                print(f"Currently playing: {vidTitle} ({vidId}) ["+' '.join(vidTags) +']')
    def create_playlist(self, playlist_name):
        list_of_all_values = []
        for i in self.playLists:
            list_of_all_values.append(i["name"])
        if playlist_name.lower().strip() in list_of_all_values:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            newEntry = {
                    "name": playlist_name.lower().strip(),
                    "alias": playlist_name,
                    "videos":[]
                }
            self.playLists.append(newEntry)
            print(f"Successfully created new playlist: {newEntry['alias']}")
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        internalListOfPlaylists = []
        internalVideoList = []
        for i in self.playLists:
            internalListOfPlaylists.append(i['name'])
        for v in self._video_library.get_all_videos():
            internalVideoList.append(v.video_id)

        
        if playlist_name.lower().strip() not in internalListOfPlaylists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        else:
            if video_id not in internalVideoList:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            else:
                for i in self.playLists:
                    if playlist_name.lower().strip() == i['name']:
                        if video_id in i["videos"]:
                            print(f"Cannot add video to {playlist_name}: Video already added")
                        else:
                            i["videos"].append(video_id)
                            newVidId = self._video_library.get_video(video_id)._title
                            print(f"Added video to {playlist_name}: {newVidId}")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playLists) == 0:
            print("No playlists exist yet")
        elif len(self.playLists) > 0:
            aliases = []
            print("Showing all playlists:")
            for i in self.playLists:
                aliases.append(i['alias'])
            for i in sorted(aliases):
                print(i)

        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        
        Args:
            playlist_name: The playlist name.
        """
        listOfPlaylists = []
        if len(self.playLists) == 0:
            print("No playlists exist yet")
        else:
            for i in self.playLists:
                listOfPlaylists.append(i['name'])
            
            if playlist_name.lower().strip() not in listOfPlaylists:
                print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            else :
                for i in self.playLists:
                    if i['name'] == playlist_name.lower().strip():
                        if len(i['videos']) == 0:
                            print(f"Showing playlist: {playlist_name}")
                            print("No videos here yet")
                        elif len(i['videos']) > 0:
                            print(f"Showing playlist: {playlist_name}")
                            for k in i['videos']:
                                vidTitle = self._video_library.get_video(k)._title
                                vidId = self._video_library.get_video(k).video_id
                                vidTags = self._video_library.get_video(k).tags
                                print(f"{vidTitle} ({vidId}) ["+' '.join(vidTags) +']')
            
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        localPlayLists = []
        videoPlaylist = []
        for i in self.playLists:
            localPlayLists.append(i['name'])
        for i in self._video_library.get_all_videos():
            videoPlaylist.append(i.video_id)
        if playlist_name.lower().strip() not in localPlayLists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")    
        elif video_id not in videoPlaylist:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif video_id in videoPlaylist:
            index = 0
            for i in self.playLists:
                if playlist_name.lower().strip() == i['name']:
                    if video_id not in i['videos']:
                        print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                    for j in i['videos']:
                        if video_id == j:
                            self.playLists[index]['videos'].remove(j)
                            videoName = self._video_library.get_video(video_id)._title
                            print(f"Removed video from {playlist_name}: {videoName}")
                index+=1

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playList_local = []
        for i in self.playLists:
            playList_local.append(i['name'])
        index = 0
        if playlist_name.lower().strip() not in playList_local:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            for i in self.playLists:
                if playlist_name.lower().strip() == i['name']:
                    for j in i['videos']:
                        self.playLists[index]['videos'].remove(j)
                index +=1

            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        temp_playlists = []
        for i in self.playLists:
            temp_playlists.append(i['name'])
             
        if playlist_name.lower().strip() not in temp_playlists:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:

            for i in self.playLists:
                if playlist_name.lower().strip() in i['name']:
                    self.playLists.remove(i)
                    print(f"Deleted playlist: {playlist_name}")

        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = []
        datalist = self._video_library.get_all_videos()
        for i in datalist:
            videos.append(
                {
                    'name':i._title,
                    'video_id':i.video_id,
                    'tags':i.tags
                }
            )
        foundItems = []
        for i in videos:
            if search_term.lower().strip() in i['name'].lower().strip():
                foundItems.append(i)
        index = 1
        if len(foundItems) > 0:
            print(f"Here are the results for {search_term}:")
            for i in foundItems:
                print(f"{index}) {i['name']} ({i['video_id']}) ["+' '.join(i['tags'])+']\n')
                index +=1
            userChoice = input("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            if "no" in userChoice.lower().strip(): 
                pass
            else:
                try:
                    usernum = int(userChoice) -1
                    print(f"Playing video: {foundItems[usernum]['name']}")
                    
                except Exception as e:
                    pass
        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = []
        datalist = self._video_library.get_all_videos()
        for i in datalist:
            videos.append(
                {
                    'name':i._title,
                    'video_id':i.video_id,
                    'tags':i.tags
                }
            )
        foundItems = []
        for i in videos:
            if video_tag.lower().strip() in i['tags']:
                foundItems.append(i)
        
        index = 1
        if len(foundItems) > 0:
            print(f"Here are the results for {video_tag}:")
            for i in foundItems:
                print(f"{index}) {i['name']} ({i['video_id']}) ["+' '.join(i['tags'])+']\n')
                index +=1
            userChoice = input("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            if "no" in userChoice.lower().strip(): 
                pass
            else:
                try:
                    usernum = int(userChoice) -1
                    print(f"Playing video: {foundItems[usernum]['name']}")
                    
                except Exception as e:
                    pass
        else:
            print(f"No search results for {video_tag}")

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        idList = []
        
        datalist = self._video_library.get_all_videos()
        for i in datalist:
            idList.append(i.video_id)
        foundItems = []
        

        if video_id not in idList:
            print("Cannot flag video: Video does not exist")
        elif video_id in idList:
            for i in self.tagList:
                if i['flagged'] == True:
                    if i['video_id'] == video_id:
                        print("Cannot flag video: Video is already flagged")
                elif  i['flagged'] == False:
                    if i['video_id'] == video_id:
                        i['flagged'] = True
                        if flag_reason != 'Not supplied':
                            i['flag_reason'] = flag_reason
                        print(f"Successfully flagged video: {i['name']} (reason: {i['flag_reason']})")
        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
