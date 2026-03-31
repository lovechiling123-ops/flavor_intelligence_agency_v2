import re

file_path = "C:/Users/tokchou/.gemini/antigravity/scratch/flavor_intelligence_agency/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix backslash escapes
content = content.replace(r'\`', '`')
content = content.replace(r'\${', '${')

# Replace Firebase logic
auth_firebase_logic = """        // 單機版認證與監聽
        const initAuth = async () => {
            try {
                if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
                    await signInWithCustomToken(auth, __initial_auth_token);
                } else { await signInAnonymously(auth); }
            } catch (err) { authStatus.innerText = "AUTH ERROR"; }
        };

        onAuthStateChanged(auth, (u) => {
            user = u;
            if (user) { authStatus.innerText = `AGENT: ${user.uid.substring(0,8)}`; startDataListener(); }
            else { authStatus.innerText = "AUTHENTICATING..."; }
        });

        const startDataListener = () => {
            if (!user) return;
            const colRef = collection(db, 'artifacts', appId, 'public', 'data', 'restaurants');
            onSnapshot(colRef, (snapshot) => {
                restaurants = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
                renderList(); initCards();
            }, (error) => { console.error("Firebase Error:", error); });
        };"""

auth_local_logic = """        // 單機版認證與監聽
        const initAuth = async () => {
            user = { uid: 'local_agent' };
            authStatus.innerText = `AGENT: LOCAL (OFFLINE)`;
            startDataListener();
        };

        const startDataListener = () => {
            try {
                const saved = localStorage.getItem(DB_KEY);
                restaurants = saved ? JSON.parse(saved) : [];
            } catch (error) {
                restaurants = [];
            }
            renderList(); 
            initCards();
        };"""

content = content.replace(auth_firebase_logic, auth_local_logic)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
