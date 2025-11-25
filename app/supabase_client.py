from supabase import create_client, Client

# Substitua pelos seus dados reais do Supabase
SUPABASE_URL = "https://xyzcompany.supabase.co"
SUPABASE_KEY = "your-anon-or-service-role-key"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
