
import os
from supabase import create_client, Client

url = "https://qadfjxzauvrjrfqahbbm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhZGZqeHphdXZyanJmcWFoYmJtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTE0MDU0NiwiZXhwIjoyMDM0NzE2NTQ2fQ.kbDbfeuQp7LvVRJsaQ4K7MoE-qkxd0p4n3HA3GH-Db8"
supabase: Client = create_client(url, key)

def check():
    response = supabase.table("Record").select("id","Password").execute()
    print(response.data)
    return response.data

def sign_up(user_id,name,mail,password):
    response = (
    supabase.table("Record")
    .insert({"id": user_id, "Name":name,"email":mail,"Password":password})
    .execute()
)