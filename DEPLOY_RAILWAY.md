# 🚂 Deploy Resume Analyzer to Railway (Effectively FREE Forever)

## ✅ Why Railway?

| Feature | Railway | Oracle Cloud | Render Free |
|---------|---------|--------------|-------------|
| **Monthly Credits** | ✅ $5 FREE (renews) | ❌ Rate limited signup | ❌ 750 hrs limit |
| **Sleep Mode** | ✅ Never | ✅ Never | ❌ 15 min timeout |
| **RAM** | ✅ Up to 8GB | ✅ 1GB | ❌ 512MB |
| **ML Support** | ✅ Full | ✅ Full | ❌ Limited |
| **Cold Starts** | ✅ Instant | ✅ Instant | ❌ 30-60s |
| **Signup** | ✅ Easy (GitHub) | ❌ Often blocked | ✅ Easy |
| **Cost** | **~$3-4/mo** (under $5) | $0 (if signup works) | $0 (limited) |

**Bottom Line:** Your ML app will use ~$3-4/month. Railway gives you $5/month FREE. **You pay $0!** ✅

---

## 🚀 Deploy in 10 Minutes

### Step 1: Create GitHub Repository (3 minutes)

**Option A: Create New Repo (Recommended)**

1. **Go to:** https://github.com/new
2. **Repository name:** `resume-analyzer`
3. **Description:** Resume Analyzer with ML - spaCy, pandas, matplotlib
4. **Visibility:** Public (for free Railway deployment)
5. **Click:** "Create repository"

**Option B: Use Existing Repo**

Skip to Step 2 if you already have a GitHub repo.

---

### Step 2: Push Your Code to GitHub (5 minutes)

**On your Windows PC (PowerShell):**

```powershell
# Navigate to project
cd C:\Projects\Resume_Analyzer

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Resume Analyzer with ML"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Enter your GitHub credentials when prompted.**

✅ Your code is now on GitHub!

---

### Step 3: Deploy to Railway (2 minutes)

1. **Go to:** https://railway.app/
2. **Click:** "Start a New Project"
3. **Login with GitHub** (authorize Railway)
4. **Click:** "Deploy from GitHub repo"
5. **Select:** `resume-analyzer` repository
6. **Click:** "Deploy Now"

**Railway will automatically:**
- ✅ Detect Flask app
- ✅ Install Python 3.11
- ✅ Install all requirements
- ✅ Download spaCy model
- ✅ Start Gunicorn server

---

### Step 4: Configure Environment (1 minute)

1. **In Railway dashboard:**
   - Click your project
   - Go to **"Variables"** tab
   
2. **Add variable:**
   ```
   PORT=8000
   ```

3. **Click:** "Settings" tab
4. **Scroll to:** "Networking"
5. **Click:** "Generate Domain"

✅ You'll get a URL like: `resume-analyzer-production.up.railway.app`

---

### Step 5: Wait for Deployment (2-3 minutes)

**Watch the build logs:**
- Installing dependencies...
- Downloading spaCy model...
- Starting Gunicorn...

**When you see:**
```
✅ Deployment successful
```

**Your app is LIVE!** 🎉

---

## 🌐 Access Your Deployment

**Your app URL:**
```
https://resume-analyzer-production.up.railway.app
```

**Test all features:**
- ✅ Upload PDF resume
- ✅ Search skills
- ✅ View analysis with charts
- ✅ Top Profiles recommendations
- ✅ Mobile responsive

---

## 💰 Monitor Usage (Stay Under $5)

### Check Your Usage:

1. **Railway Dashboard:** https://railway.app/dashboard
2. **Click:** Your project
3. **View:** "Usage" tab

**Your ML app typically uses:**
- **~$3-4/month** for always-on deployment
- **$5 FREE credits** renew every month
- **Net cost: $0** ✅

### Tips to Stay Under $5:

1. **Optimize memory usage** (Railway charges for RAM)
2. **Use sleep mode** if not needed 24/7 (optional)
3. **Monitor uploads folder** size
4. **Clear old logs** regularly

---

## 🛠️ Update Your Deployment

**When you make code changes:**

```powershell
cd C:\Projects\Resume_Analyzer

# Make your changes to app.py, templates, etc.

# Commit and push
git add .
git commit -m "Updated feature X"
git push

# Railway auto-deploys in 1-2 minutes!
```

---

## 🔧 Troubleshooting

### Issue: Build Failed

**Check logs in Railway dashboard:**

**Common fixes:**

1. **Missing requirements.txt**
   - Ensure file exists in root directory
   - Check all packages listed

2. **spaCy model download failed**
   - Railway might timeout
   - Add to `nixpacks.toml` (already done)

3. **Port binding error**
   - Check `wsgi.py` binds to `$PORT`
   - Verify `Procfile` correct

### Issue: 502 Bad Gateway

**Possible causes:**

1. **App crashed** - Check logs
2. **Wrong port** - Should use `$PORT` environment variable
3. **Startup timeout** - Increase in Railway settings

**Fix:**
```powershell
# Check app.py doesn't hardcode port 5000
# Gunicorn handles ports automatically
```

### Issue: Charts Not Displaying

**Check:**
1. Matplotlib backend set to 'Agg' (non-GUI)
2. Static files uploaded to GitHub
3. Uploads directory exists

---

## 📊 Alternative: Fly.io (Also Great)

If Railway doesn't work, try **Fly.io**:

### Fly.io Free Tier:
- ✅ 3 shared-cpu-1x VMs (256MB each)
- ✅ 3GB persistent storage
- ✅ 160GB outbound transfer
- ✅ **FREE FOREVER**

### Deploy to Fly.io:

```powershell
# Install flyctl
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Login
fly auth login

# Deploy
cd C:\Projects\Resume_Analyzer
fly launch --name resume-analyzer

# Follow prompts, accept defaults
```

**Deployment time:** 5 minutes

---

## 🔄 Third Option: Google Cloud Run

**Serverless deployment:**

### Benefits:
- ✅ 2 million requests FREE/month
- ✅ 360,000 GB-seconds memory FREE
- ✅ Scales to zero (no cost when idle)

### Drawbacks:
- ⚠️ Cold starts (3-5 seconds)
- ⚠️ Requires Docker knowledge

**Good for:** Low-traffic deployments

---

## 💡 Which Platform Should You Use?

| Use Case | Best Platform |
|----------|---------------|
| **24/7 always-on, simple setup** | **Railway** ✅ |
| **Truly free, okay with setup** | **Fly.io** |
| **Low traffic, serverless** | Google Cloud Run |
| **High traffic, paid okay** | AWS, Azure, GCP |

**Recommendation:** Start with **Railway** - easiest setup, effectively free for your use case.

---

## ✅ Success Checklist

After deployment, verify:

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project deployed on Railway
- [ ] Custom domain generated
- [ ] Application accessible via URL
- [ ] Upload feature working
- [ ] Search functionality working
- [ ] Analysis charts displaying
- [ ] Top Profiles working
- [ ] Mobile responsive
- [ ] Usage under $5/month

---

## 🎉 You're Live!

Your Resume Analyzer is now deployed with:
- ✅ **Full ML support** (spaCy, pandas, matplotlib)
- ✅ **No sleep mode** (always available)
- ✅ **Effectively FREE** ($5 credits cover usage)
- ✅ **Auto-deployment** (push to GitHub = auto-update)
- ✅ **SSL/HTTPS** (included)
- ✅ **Custom domain** (can add your own)

**Share your app:**
```
https://your-app.up.railway.app
```

---

## 📞 Need Help?

**Railway Documentation:** https://docs.railway.app/  
**Railway Discord:** https://discord.gg/railway  
**Check logs:** Railway Dashboard → Your Project → "Deployments"

**Common commands:**
```powershell
# View logs
railway logs

# Link local project
railway link

# Environment variables
railway variables
```

---

**🚂 Happy Deploying with Railway!**

*Estimated monthly cost: $0 (under free $5 credits)*
