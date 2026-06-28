from models.predict import predict_crop
from models.moisture import estimate_moisture
from models.weather import get_weather


def generate_report(parcel_id, latitude, longitude):

    prediction = predict_crop(parcel_id)

    weather = get_weather(latitude, longitude)

    moisture = estimate_moisture(parcel_id)

    if moisture >= 70:
        advice = "No irrigation required."

    elif moisture >= 50:

        if weather["rain"] > 0:
            advice = "Rain detected. Delay irrigation."

        else:
            advice = "Monitor the field. Irrigate if dry conditions continue."

    else:

        if weather["rain"] > 0:
            advice = "Rain expected. Wait before irrigating."

        else:
            advice = "Immediate irrigation recommended."

    return {

        "crop": prediction["crop_name"],

        "confidence": prediction["confidence"],

        "moisture": moisture,

        "temperature": weather["temperature"],

        "humidity": weather["humidity"],

        "rain": weather["rain"],

        "advice": advice
    }