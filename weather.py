sessionId = data.get("sessionId")
temperature = data.get("temperature")
wind_speed = data.get("wind_speed")
precipitation_probability = data.get("precipitation_probability") 
weather = data.get("weather")

verb = "este"

if weather == "puțini nori":
    verb = "sunt"

if wind_speed < 2:
    text_vant = "este calm, viteza vântului fiind de"
if wind_speed > 2 and wind_speed < 6:
    text_vant = "este vânt abia perceptibil cu o viteză de"
if wind_speed > 7 and wind_speed < 11:
    text_vant = "este vânt foarte ușor și bate cu o viteză de"
if wind_speed > 11 and wind_speed < 20:
    text_vant = "este vânt ușor și bate cu o viteză de"
if wind_speed > 20 and wind_speed < 29:
    text_vant = "este vânt moderat și bate cu o viteză de"
if wind_speed > 29 and wind_speed < 36:
    text_vant = "este vânt semnificati și bate cu o viteză dev"
if wind_speed > 36 and wind_speed < 50:
    text_vant = "este vânt puternic și bate cu o viteză de"
if wind_speed > 50 and wind_speed < 61:
    text_vant = "este vânt vânt foarte puternic și bate cu o viteză de"
if wind_speed > 61 and wind_speed < 72:
    text_vant = "este vânt extrem de puternic și bate cu o viteză de"
if wind_speed > 72 and wind_speed < 86:
    text_vant = "este început de furtună și vântul bate cu o viteză de"
if wind_speed > 86 and wind_speed < 101:
    text_vant = "este furtună și vântul bate cu o viteză de"
if wind_speed > 101 and wind_speed < 115:
    text_vant = "este furtună violentă și vântul bate cu o viteză de"
if wind_speed > 115:
    text_vant = "este uragan și vântul bate cu o viteză de"
payload_template = '{"sessionId": "' + str(sessionId) + '", "text": "temperatura de afara este ' + str(temperature) + ' grade ' + str(text_vant) + str(wind_speed) + ' kilometri pe oră, probabilitatea de precipitații este de ' + str(precipitation_probability) + ' la sută, și ' + str(verb) + ' ' + str(weather) + '"}'

service_data = {
    "topic": "hermes/dialogueManager/endSession",
    "payload_template": payload_template
}

hass.services.call("mqtt", "publish", service_data, False)