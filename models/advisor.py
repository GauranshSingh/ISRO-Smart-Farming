from models.predict import predict_crop
from models.moisture import estimate_moisture
from models.weather import get_weather


def smart_advisor(parcel_id):

    prediction = predict_crop(parcel_id)
    print(prediction)

    crop_name = prediction["crop_name"]
    confidence = prediction["confidence"]

    # Temporary coordinates (Jaipur)
    latitude = 26.9124
    longitude = 75.7873

    weather = get_weather(latitude, longitude)

    moisture = estimate_moisture(parcel_id)

    if moisture >= 70:
        english = "No irrigation required."
        hindi = "सिंचाई की आवश्यकता नहीं है।"

    elif moisture >= 50:

        if weather["rain"] > 0:
            english = "Rain detected. Delay irrigation."
            hindi = "बारिश की संभावना है। सिंचाई कुछ समय बाद करें।"

        else:
            english = "Monitor the field. Irrigate if dry conditions continue."
            hindi = "खेत की निगरानी करें। यदि सूखा बना रहे तो सिंचाई करें।"

    else:

        if weather["rain"] > 0:
            english = "Rain expected. Wait before irrigating."
            hindi = "बारिश की संभावना है। सिंचाई करने से पहले प्रतीक्षा करें।"

        else:
            english = "Immediate irrigation recommended."
            hindi = "तुरंत सिंचाई करने की सलाह दी जाती है।"

    return {

        "label": prediction["label"],

        "crop_name": crop_name,

        "confidence": confidence,

        "moisture": moisture,

        "temperature": weather["temperature"],

        "humidity": weather["humidity"],

        "rain": weather["rain"],

        "english": english,

        "hindi": hindi
    }