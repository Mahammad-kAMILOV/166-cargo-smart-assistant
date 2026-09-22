# 1. BİZNES DATASI (Daxili Anbar Bazasının Məlumatları)  DICTIONARY KEY-VALUE CUTLERI ISTIFADE EDIRIK
CARGO_DATABASE = [
    {
        "tracking_id": "166-AZ-101",
        "customer": "Əli Məmmədov",
        "status": "Yoldadır (Kuryerdə)",
        "destination": "Yasamal rayonu, M.Fətəli küç. 12",
        "weight_kg": 4.5,
        "delivery_fee_azn": 6.0
    },
    {
        "tracking_id": "166-AZ-102",
        "customer": "Ləman Əliyeva",
        "status": "Anbardadır",
        "destination": "Gənclik m/s yaxınlığı",
        "weight_kg": 1.2,
        "delivery_fee_azn": 3.0
    },
    {
        "tracking_id": "166-AZ-103",
        "customer": "Məhəmməd Kamilov",
        "status": "Çatdırıldı",
        "destination": "Badamdar qəsəbəsi, 3-cü yaşayış massivi",
        "weight_kg": 12.0,
        "delivery_fee_azn": 15.0
    }
]

# 2. RETRIEVAL STEP (RAG-ın Axtarış Hissəsi)
def retrieve_cargo_info(tracking_id: str) -> dict:
    clean_id = tracking_id.strip().upper()
    for cargo in CARGO_DATABASE:
        if cargo["tracking_id"] == clean_id:
            return cargo
    return None

# 3. GENERATION STEP (Cavab Yaratmaq Hissəsi)
def generate_ai_response(user_query: str, tracking_id: str) -> str:
    cargo_data = retrieve_cargo_info(tracking_id)
    
    if not cargo_data:
        return f"❌ Bağışlayın, [{tracking_id.strip().upper()}] nömrəli karqo sistemdə tapılmadı."

    context = (
        f"Müştəri: {cargo_data['customer']}\n"
        f"Status: {cargo_data['status']}\n"
        f"Ünvan: {cargo_data['destination']}\n"
        f"Çəki: {cargo_data['weight_kg']} kg\n"
        f"Çatdırılma haqqı: {cargo_data['delivery_fee_azn']} AZN"
    )

    ai_response = (
        f"Salam, {cargo_data['customer']}! 👋\n"
        f"Sizin [{cargo_data['tracking_id']}] nömrəli bağlamanızın cari statusu: **{cargo_data['status']}**.\n"
        f"Çatdırılma ünvanı: {cargo_data['destination']}.\n"
        f"Ödəniləcək məbləğ: {cargo_data['delivery_fee_azn']} AZN."
    )
    return ai_response

# 4. İNTERAKTİV DÖVR (WHILE LOOP İLƏ TƏKRAR SORĞULAR)
if __name__ == "__main__":
    print("=== 166 LOGISTICS SMART AI ASSISTANT (RAG PROTOTYPE) ===")
    print("Çıxış etmək üçün 'exit' və ya 'q' yazın.\n")
    
    # while True proqramı biz bağlayana qədər sonsuz işlədir
    while True:
        tracking_id = input("📦 Karqo Tracking ID daxil edin (məs: 166-AZ-101): ")
        
        # Çıxış şərti
        if tracking_id.strip().lower() in ['exit', 'q']:
            print("\nSistemdən çıxıldı. Sağ olun!")
            break
            
        user_question = input("❓ Sualınızı yazın (məs: Bağlamam haradadır?): ")
        
        # Çıxış şərti
        if user_question.strip().lower() in ['exit', 'q']:
            print("\nSistemdən çıxıldı. Sağ olun!")
            break
            
        print("\n🤖 AI Asistenti Cavablandırır...")
        print("-" * 50)
        response = generate_ai_response(user_question, tracking_id)
        print(response)
        print("=" * 50 + "\n")