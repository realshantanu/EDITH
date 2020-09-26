import pafy  
  
url = input("Enter Youtube Link:   ")

video = pafy.new(url) 
  
bestaudio = video.getbestaudio() 
bestaudio.download("C:\\Users\\Shantanu\\Downloads\\youtube") 
