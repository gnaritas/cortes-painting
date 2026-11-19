# DEPLOY — Cortés Painting Inc (cohort B, 2026-11-19)
- Live preview: https://cortes-painting-demo.up.railway.app
- Repo: github.com/gnaritas/cortes-painting
- Railway: project fd4076a1-e110-4dc9-81a2-d53c1bad0e7e / service 2b36731b-5f96-41b1-bb28-945c2bf13ded; env BREVO_API_KEY set
- Gotcha: first deploy lacked server.js (Railway served bare static: no /healthz /pixel /open, POST 405). Fix = copy instrumented server.js + package.json + pixel.gif from sibling, redeploy. Always `ls server.js package.json` before first `railway up`.
- Identity: forest & limestone, bristle strips, LBPR lead-safe copy. CCB #213757 ACTIVE, LBPR thru 2027, bonded/insured per CCB record. FB facebook.com/cortespaintinginc sameAs. Homonyms excluded.
- Verification: _verify.py PASS 0/0; 14-route walk; og md5 live==local ffc42500...; POST 303; CONTACT+MAILSENT in railway logs 23:56Z; render sweep clean (CDP)
