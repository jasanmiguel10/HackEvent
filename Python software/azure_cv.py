from unicode import unicode
##n 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import sys
###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '2c00fc02de7b430da1943171f669ce34'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'eastus2.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

import codecs
list_url = []
diction = {}
with codecs.open(sys.argv[1],'r',encoding='utf-8') as f:
        count =0
        for line in f:
                line = line.strip()
                #list_url.append(line)
                if count == 0:
                        count = 1
                else:
                        list_url.append(line)
texto = {}
count = 0
for item in list_url:
        obj = {'url':item}
        #print (obj)
# Replace the three dots below with the URL of a JPEG image of a celebrity.
        body = str(obj)#"{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"
        print (body)
        try:
        # Execute the REST API call and get the response.
                conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
                conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
                response = conn.getresponse()
                data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
                parsed = json.loads(data)
                #print(parsed['description']['captions'])
                print ("Response:")
                txt = json.dumps(parsed['description']['captions'][0]['text'],sort_keys=True,indent=2)
                print (txt)
                texto[count] = txt
                #print (json.dumps(parsed['description']['captions'], sort_keys=True, indent=2))
                #print (descri)
                conn.close()
                count = count +1
        except Exception as e:
                print('Error:')
                print(e)
with open('ids_captios.data','w') as out:
        for key, value in texto.items():
                text_ = str(list_url[key]) +'\t' + str(value) + '\n'
                out.write(text_)

####################################
                                                                                                   

