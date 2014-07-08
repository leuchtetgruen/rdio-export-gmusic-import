$: << "."
require 'json'
require 'rdio'


rdio = Rdio.new(["consumerkey", "consumersecret"])

# authenticate against the Rdio service
url = rdio.begin_authentication('oob')
puts 'Go to: ' + url
print 'Then enter the code: '
verifier = gets.strip
rdio.complete_authentication(verifier)


tracks = rdio.call("getTracksInCollection")

tracks_json = tracks["result"].map do |t|
	p t
	if (t["name"] and t["artist"] and t["album"]) then
		{
			:title => t["name"],
			:artist => t["artist"],
			:album => t["album"]
		}
	else
		nil
	end
end.compact

s_json = tracks_json.to_json

p tracks_json
File.write("tracks.json", s_json)
