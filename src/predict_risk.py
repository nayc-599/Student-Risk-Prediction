def predict_risk(user_df, model, scaler):
    user_data_scaled = scaler.transform(user_df)
    predicted_risk_level = int(model.predict(user_data_scaled)[0])

    risk_level_map = {
    0: "Low",
    1: "Moderate",
    2: "High",
    3: "Very High"
}

    risk_level = risk_level_map[predicted_risk_level]

    return user_data_scaled, predicted_risk_level, risk_level