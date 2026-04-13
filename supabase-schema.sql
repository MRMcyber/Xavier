-- SQL Script to set up the Fact Check History Table in Supabase
-- Paste this into the Supabase SQL Editor and hit run.

-- 1. Create the table
CREATE TABLE fact_check_history (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES auth.users NOT NULL,
  claim TEXT NOT NULL,
  verdict VARCHAR(50) NOT NULL,
  explanation TEXT,
  source_links JSONB DEFAULT '[]'::jsonb,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Enable Row Level Security (RLS) so users can't see each other's data
ALTER TABLE fact_check_history ENABLE ROW LEVEL SECURITY;

-- 3. Create Policy: Users can see their own history
CREATE POLICY "Users can read own history" 
ON fact_check_history
FOR SELECT
USING (auth.uid() = user_id);

-- 4. Create Policy: Authenticated users can insert their own history
-- Note: Often, the FastAPI backend will insert this via the service_role key, 
-- which bypasses RLS. But if the frontend inserts it, they need this:
CREATE POLICY "Users can insert own history" 
ON fact_check_history
FOR INSERT
WITH CHECK (auth.uid() = user_id);
