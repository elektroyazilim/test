message = "htts://www.kodlanir.com"
# print(message[0])
# print(message[:7])

webSite = "htts://www.kodlanir.com"
message = "shadow"

result = webSite + " " + message
print(result)

message = "kodlanir"
webSite = "htts://www.kodlanir.com"
print(message in webSite)

print(webSite.__contains__(message))

webSite = "htts://www.kodlanir.com"
print(webSite)

result = webSite.split(".")
print(result)
print(result[1])

webSite = "   htts://www.kodlanir.com     "
print(webSite)
print(webSite.strip())

message = "******kodlanir******"
print(message)
print(message.strip("*"))

message = "******kodlanir******"
print(message)
print(message.lstrip("*"))
