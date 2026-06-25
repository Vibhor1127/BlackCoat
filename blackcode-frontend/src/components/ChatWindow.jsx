import { useState, useRef, useEffect } from 'react';
import axios from 'axios';

const LadyJustice = ({ animate }) => (
  <svg width="120" height="180" viewBox="0 0 120 180" fill="none" xmlns="http://www.w3.org/2000/svg"
    style={{ filter: 'drop-shadow(0 4px 24px rgba(201,168,76,0.18))' }}>
    <defs>
      <radialGradient id="robeGrad" cx="50%" cy="60%" r="50%">
        <stop offset="0%" stopColor="#2C2F3A" />
        <stop offset="100%" stopColor="#0B0F1A" />
      </radialGradient>
    </defs>
    <line x1="60" y1="38" x2="60" y2="80" stroke="#C9A84C" strokeWidth="1.5" />
    <line x1="30" y1="50" x2="90" y2="50" stroke="#C9A84C" strokeWidth="1.5" />
    <line x1="30" y1="50" x2="30" y2="70" stroke="#C9A84C" strokeWidth="1" />
    <line x1="90" y1="50" x2="90" y2="70" stroke="#C9A84C" strokeWidth="1" />
    <ellipse cx="30" cy="72" rx="12" ry="4" fill="none" stroke="#C9A84C" strokeWidth="1.2"
      style={{ transformOrigin: '30px 50px', animation: animate ? 'swayLeft 2.5s ease-in-out infinite alternate' : 'idleSway 4s ease-in-out infinite alternate' }} />
    <ellipse cx="90" cy="72" rx="12" ry="4" fill="none" stroke="#C9A84C" strokeWidth="1.2"
      style={{ transformOrigin: '90px 50px', animation: animate ? 'swayRight 2.5s ease-in-out infinite alternate' : 'idleSway2 4s ease-in-out 2s infinite alternate' }} />
    <ellipse cx="60" cy="28" rx="12" ry="13" fill="#2C2F3A" />
    <rect x="48" y="25" width="24" height="6" rx="3" fill="#8B1A1A" />
    <path d="M50 20 Q55 16 60 19 Q65 16 70 20" stroke="#C9A84C" strokeWidth="1.2" fill="none" />
    <path d="M45 41 Q38 80 34 140 Q46 145 60 145 Q74 145 86 140 Q82 80 75 41 Q68 38 60 38 Q52 38 45 41Z"
      fill="url(#robeGrad)" stroke="#2C2F3A" strokeWidth="0.5" />
    <path d="M55 45 Q52 90 50 138" stroke="#C9A84C" strokeWidth="0.4" strokeOpacity="0.3" />
    <path d="M65 45 Q67 90 68 138" stroke="#C9A84C" strokeWidth="0.4" strokeOpacity="0.3" />
    <path d="M75 55 Q90 48 95 42" stroke="#2C2F3A" strokeWidth="8" strokeLinecap="round" />
    <path d="M75 55 Q90 48 95 42" stroke="#3A3F50" strokeWidth="5" strokeLinecap="round" />
    <path d="M45 60 Q28 68 22 75" stroke="#2C2F3A" strokeWidth="8" strokeLinecap="round" />
    <path d="M45 60 Q28 68 22 75" stroke="#3A3F50" strokeWidth="5" strokeLinecap="round" />
    <line x1="22" y1="75" x2="10" y2="110" stroke="#C9A84C" strokeWidth="1.5" />
    <line x1="18" y1="78" x2="26" y2="78" stroke="#C9A84C" strokeWidth="1.5" />
    <rect x="42" y="140" width="36" height="8" rx="2" fill="#1A1D28" stroke="#C9A84C" strokeWidth="0.5" />
    <rect x="36" y="148" width="48" height="6" rx="2" fill="#14172030" stroke="#C9A84C" strokeWidth="0.5" />
    <style>{`
      @keyframes idleSway { 0%{transform:rotate(-3deg)}100%{transform:rotate(3deg)} }
      @keyframes idleSway2 { 0%{transform:rotate(3deg)}100%{transform:rotate(-3deg)} }
      @keyframes swayLeft { 0%{transform:rotate(-8deg) translateY(2px)}100%{transform:rotate(2deg) translateY(-2px)} }
      @keyframes swayRight { 0%{transform:rotate(2deg) translateY(-2px)}100%{transform:rotate(-8deg) translateY(2px)} }
    `}</style>
  </svg>
);

const GavelStrike = ({ trigger }) => {
  const [show, setShow] = useState(false);
  useEffect(() => {
    if (trigger) { setShow(true); const t = setTimeout(() => setShow(false), 900); return () => clearTimeout(t); }
  }, [trigger]);
  if (!show) return null;
  return (
    <div style={{ position:'fixed', top:'50%', left:'50%', transform:'translate(-50%,-50%)', zIndex:9999, pointerEvents:'none' }}>
      <div style={{ animation:'gavelPop 0.9s ease forwards' }}>
        <svg width="80" height="80" viewBox="0 0 80 80">
          <rect x="28" y="18" width="32" height="14" rx="4" fill="#C9A84C" transform="rotate(-35 44 25)" />
          <rect x="34" y="30" width="6" height="34" rx="3" fill="#8B6914" transform="rotate(-35 37 47)" />
          <circle cx="40" cy="40" r="38" fill="none" stroke="#C9A84C" strokeWidth="1" opacity="0.4"
            style={{ animation:'ripple 0.9s ease forwards' }} />
        </svg>
      </div>
      <style>{`
        @keyframes gavelPop { 0%{opacity:0;transform:scale(0.3) rotate(-40deg)} 30%{opacity:1;transform:scale(1.2) rotate(5deg)} 60%{opacity:1;transform:scale(1) rotate(0deg)} 100%{opacity:0;transform:scale(1.1) rotate(0deg)} }
        @keyframes ripple { 0%{r:0;opacity:0.6} 100%{r:60;opacity:0} }
      `}</style>
    </div>
  );
};

// Renders structured argument sections with icons
const ArgumentBlock = ({ text }) => {
  const sections = [
    { key: '⚖️ LEGAL POSITION',     color: '#C9A84C', bg: 'rgba(201,168,76,0.08)',   border: 'rgba(201,168,76,0.3)' },
    { key: '📜 APPLICABLE LAWS',    color: '#7eb8f7', bg: 'rgba(126,184,247,0.06)',  border: 'rgba(126,184,247,0.25)' },
    { key: '🗣️ THE ARGUMENT',       color: '#a8d8a8', bg: 'rgba(168,216,168,0.06)',  border: 'rgba(168,216,168,0.25)' },
    { key: '📋 SUPPORTING JUDGMENTS', color: '#f7c87e', bg: 'rgba(247,200,126,0.06)', border: 'rgba(247,200,126,0.25)' },
    { key: '✅ WHAT YOU CAN DO RIGHT NOW', color: '#b8f7b8', bg: 'rgba(184,247,184,0.06)', border: 'rgba(184,247,184,0.25)' },
    { key: '⚠️ IMPORTANT',          color: '#f78e7e', bg: 'rgba(247,142,126,0.06)',  border: 'rgba(247,142,126,0.2)' },
  ];

  // Try to parse sections
  let parsed = [];
  let remaining = text;

  sections.forEach(s => {
    const idx = remaining.indexOf(s.key);
    if (idx !== -1) {
      const afterHeading = remaining.indexOf('\n', idx);
      const nextSectionIdxes = sections
        .map(s2 => remaining.indexOf(s2.key, idx + 1))
        .filter(i => i > idx);
      const end = nextSectionIdxes.length ? Math.min(...nextSectionIdxes) : remaining.length;
      const content = remaining.slice(afterHeading, end).trim();
      parsed.push({ ...s, content });
    }
  });

  // If parsing fails, just show raw text nicely
  if (parsed.length === 0) {
    return (
      <div style={{ color:'#F5F0E8', fontSize:'14px', lineHeight:'1.8', whiteSpace:'pre-wrap' }}>
        {text}
      </div>
    );
  }

  return (
    <div style={{ display:'flex', flexDirection:'column', gap:'10px' }}>
      {parsed.map((s, i) => (
        <div key={i} style={{
          background: s.bg,
          border: `1px solid ${s.border}`,
          borderRadius: '10px',
          padding: '12px 16px',
        }}>
          <div style={{
            color: s.color,
            fontFamily: "'Playfair Display', serif",
            fontSize: '13px',
            fontWeight: 700,
            marginBottom: '8px',
            letterSpacing: '0.3px'
          }}>
            {s.key}
          </div>
          <div style={{
            color: '#F5F0E8',
            fontSize: '13.5px',
            lineHeight: '1.8',
            whiteSpace: 'pre-wrap'
          }}>
            {s.content}
          </div>
        </div>
      ))}
    </div>
  );
};

const SourceCard = ({ source }) => (
  <div style={{
    background: 'rgba(201,168,76,0.04)',
    border: '1px solid rgba(201,168,76,0.15)',
    borderRadius: '10px',
    padding: '12px 14px',
    marginTop: '6px'
  }}>
    <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center', marginBottom:'6px', flexWrap:'wrap', gap:'6px' }}>
      <span style={{ color:'#C9A84C', fontFamily:"'Playfair Display', serif", fontSize:'13px', fontWeight:700 }}>
        {source.title}
      </span>
      <div style={{ display:'flex', gap:'6px', alignItems:'center' }}>
        {source.relevance_score && (
          <span style={{
            fontSize:'11px', padding:'2px 8px', borderRadius:'4px',
            background:'rgba(201,168,76,0.12)', color:'#C9A84C',
            border:'1px solid rgba(201,168,76,0.25)', fontFamily:"'JetBrains Mono', monospace"
          }}>
            {source.relevance_score}% match
          </span>
        )}
        <span style={{
          fontSize:'11px', padding:'2px 8px', borderRadius:'4px',
          background: source.status === 'In force' ? 'rgba(74,160,74,0.15)' : 'rgba(139,26,26,0.15)',
          color: source.status === 'In force' ? '#7fcf7f' : '#cf7f7f',
          border:`1px solid ${source.status === 'In force' ? 'rgba(74,160,74,0.3)' : 'rgba(139,26,26,0.3)'}`,
        }}>
          {source.status}
        </span>
      </div>
    </div>
    <div style={{ display:'flex', gap:'12px', marginBottom:'8px', flexWrap:'wrap' }}>
      <span style={{ fontSize:'11px', color:'#9A9A8A' }}>📋 {source.court_or_source}</span>
      <span style={{ fontSize:'11px', color:'#9A9A8A' }}>📅 {source.year}</span>
      <span style={{ fontSize:'11px', color:'#7eb8f7', fontFamily:"'JetBrains Mono', monospace" }}>
        {source.provision_id}
      </span>
    </div>
    {source.case_1 && source.case_1 !== 'nan' && (
      <div style={{ borderTop:'1px solid rgba(201,168,76,0.1)', paddingTop:'8px', marginBottom:'6px' }}>
        <div style={{ fontSize:'10px', color:'#C9A84C', marginBottom:'3px', textTransform:'uppercase', letterSpacing:'0.8px' }}>
          Landmark Case
        </div>
        <div style={{ fontSize:'12px', color:'#F5F0E8', fontStyle:'italic', marginBottom:'3px' }}>
          {source.case_1} ({source.case_1_year})
        </div>
        <div style={{ fontSize:'12px', color:'#9A9A8A', lineHeight:'1.5' }}>→ {source.case_1_holding}</div>
      </div>
    )}
    {source.case_2 && source.case_2 !== 'nan' && (
      <div style={{ borderTop:'1px solid rgba(201,168,76,0.08)', paddingTop:'8px' }}>
        <div style={{ fontSize:'12px', color:'#F5F0E8', fontStyle:'italic', marginBottom:'3px' }}>
          {source.case_2} ({source.case_2_year})
        </div>
        <div style={{ fontSize:'12px', color:'#9A9A8A', lineHeight:'1.5' }}>→ {source.case_2_holding}</div>
      </div>
    )}
    <a
      href={`https://indiankanoon.org/search/?formInput=${encodeURIComponent(source.case_1 !== 'nan' ? source.case_1 : source.title)}`}
      target="_blank"
      rel="noreferrer"
      style={{
        display:'inline-block', marginTop:'10px',
        fontSize:'11px', color:'#7eb8f7',
        textDecoration:'none', borderBottom:'1px solid rgba(126,184,247,0.3)',
        paddingBottom:'1px'
      }}
    >
      🔗 View on Indian Kanoon →
    </a>
  </div>
);

const TypingIndicator = () => (
  <div style={{ display:'flex', gap:'6px', alignItems:'center', padding:'14px 16px',
    background:'rgba(44,47,58,0.5)', borderRadius:'12px', width:'fit-content' }}>
    {[0,1,2].map(i => (
      <div key={i} style={{
        width:'7px', height:'7px', borderRadius:'50%', background:'#C9A84C',
        animation:`bounce 1.2s ${i*0.2}s infinite ease-in-out`
      }} />
    ))}
    <style>{`@keyframes bounce{0%,80%,100%{transform:translateY(0);opacity:0.5}40%{transform:translateY(-7px);opacity:1}}`}</style>
  </div>
);

const suggestions = [
  "Police arrested my brother at night without telling him why and haven't produced him before a magistrate in 36 hours",
  "My landlord locked my house and threw out my belongings without any court order",
  "My employer fired me without any notice or reason after 5 years of service",
  "Government wants to acquire our ancestral land without giving proper compensation"
];

export default function ChatWindow() {
  const [messages, setMessages] = useState([{
    role: 'bot',
    text: "Namaste. I am BlackCode — your Indian legal advocate.\n\nDescribe your situation in detail and I will identify the exact laws that apply, build a legal argument for you, and cite the Supreme Court judgments that support your case.",
    sources: []
  }]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [gavelTrigger, setGavelTrigger] = useState(0);
  const [scalesAnimate, setScalesAnimate] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const sendMessage = async (query) => {
    const q = (query || input).trim();
    if (!q || loading) return;
    setMessages(prev => [...prev, { role:'user', text:q, sources:[] }]);
    setInput('');
    setLoading(true);
    setScalesAnimate(true);
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/chat', { query: q });
      setMessages(prev => [...prev, { role:'bot', text:res.data.answer, sources:res.data.sources }]);
      setGavelTrigger(t => t + 1);
    } catch {
      setMessages(prev => [...prev, {
        role:'bot',
        text:'The backend is unreachable. Please ensure the FastAPI server is running on port 8000.',
        sources:[]
      }]);
    } finally {
      setLoading(false);
      setScalesAnimate(false);
    }
  };

  const handleKey = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  };

  return (
    <div style={{ display:'flex', height:'100vh', background:'#0B0F1A', fontFamily:"'Source Serif 4','Georgia',serif", overflow:'hidden' }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Source+Serif+4:wght@300;400&family=JetBrains+Mono:wght@400&display=swap');
        ::-webkit-scrollbar{width:4px} ::-webkit-scrollbar-track{background:transparent} ::-webkit-scrollbar-thumb{background:rgba(201,168,76,0.25);border-radius:2px}
        textarea:focus{outline:none} textarea{resize:none;font-family:inherit}
        .send-btn:hover{background:rgba(201,168,76,0.15)!important}
        .send-btn:disabled{opacity:0.35;cursor:not-allowed}
        .chip:hover{background:rgba(201,168,76,0.12)!important;border-color:rgba(201,168,76,0.5)!important}
        @media(max-width:700px){.sidebar{display:none!important}}
        @keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
        @keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
      `}</style>

      <GavelStrike trigger={gavelTrigger} />

      {/* Sidebar */}
      <div className="sidebar" style={{
        width:'220px', minWidth:'220px', background:'#0E1220',
        borderRight:'1px solid rgba(201,168,76,0.12)',
        display:'flex', flexDirection:'column', alignItems:'center',
        padding:'36px 16px 24px', gap:'20px', overflowY:'auto'
      }}>
        <LadyJustice animate={scalesAnimate} />
        <div style={{ textAlign:'center' }}>
          <div style={{ fontFamily:"'Playfair Display',serif", color:'#C9A84C', fontSize:'20px', fontWeight:700, letterSpacing:'1px' }}>BlackCode</div>
          <div style={{ color:'#9A9A8A', fontSize:'11px', marginTop:'4px', letterSpacing:'2px', textTransform:'uppercase' }}>Legal Assistant</div>
        </div>
        <div style={{ width:'100%', height:'1px', background:'rgba(201,168,76,0.12)' }} />
        <div style={{ width:'100%' }}>
          <div style={{ fontSize:'10px', color:'#9A9A8A', letterSpacing:'2px', textTransform:'uppercase', marginBottom:'10px' }}>Covers</div>
          {['Constitution of India','Landmark SC/HC Cases','Statutory Laws','Fundamental Rights','Constitutional Amendments','International Treaties'].map(t => (
            <div key={t} style={{ fontSize:'12px', color:'#6A6A5A', padding:'5px 0', borderBottom:'1px solid rgba(201,168,76,0.06)' }}>{t}</div>
          ))}
        </div>
        <div style={{ marginTop:'auto', fontSize:'10px', color:'#4A4A3A', textAlign:'center', lineHeight:'1.5' }}>
          Powered by Indian Law Database 2026
        </div>
      </div>

      {/* Main */}
      <div style={{ flex:1, display:'flex', flexDirection:'column', overflow:'hidden' }}>

        {/* Header */}
        <div style={{ padding:'16px 24px', borderBottom:'1px solid rgba(201,168,76,0.12)', display:'flex', justifyContent:'space-between', alignItems:'center', background:'#0B0F1A' }}>
          <div>
            <div style={{ fontFamily:"'Playfair Display',serif", color:'#F5F0E8', fontSize:'18px' }}>
              Nyay Kendra <span style={{ color:'#C9A84C', fontStyle:'italic' }}>/ Justice Centre</span>
            </div>
            <div style={{ fontSize:'12px', color:'#9A9A8A', marginTop:'2px' }}>Describe your situation — get a legal argument built for you</div>
          </div>
          <div style={{ width:'10px', height:'10px', borderRadius:'50%', background:'#4caf50', boxShadow:'0 0 6px rgba(76,175,80,0.5)', animation:'pulse 2s infinite' }} />
        </div>

        {/* Messages */}
        <div style={{ flex:1, overflowY:'auto', padding:'24px 20px', display:'flex', flexDirection:'column', gap:'20px' }}>
          {messages.map((msg, i) => (
            <div key={i} style={{ display:'flex', flexDirection:'column', alignItems: msg.role==='user' ? 'flex-end' : 'flex-start', animation:'fadeIn 0.3s ease' }}>
              {msg.role === 'bot' && (
                <div style={{ fontSize:'11px', color:'#C9A84C', letterSpacing:'1.5px', textTransform:'uppercase', marginBottom:'6px', fontFamily:"'JetBrains Mono',monospace" }}>
                  ⚖ BlackCode
                </div>
              )}
              <div style={{
                maxWidth: msg.role==='user' ? '65%' : '90%',
                width: msg.role==='bot' ? '90%' : 'auto',
                background: msg.role==='user' ? 'linear-gradient(135deg,rgba(139,26,26,0.25),rgba(139,26,26,0.12))' : 'rgba(20,24,38,0.85)',
                border: msg.role==='user' ? '1px solid rgba(139,26,26,0.4)' : '1px solid rgba(201,168,76,0.14)',
                borderRadius: msg.role==='user' ? '16px 16px 4px 16px' : '4px 16px 16px 16px',
                padding:'14px 18px',
              }}>
                {msg.role === 'bot' && i > 0
                  ? <ArgumentBlock text={msg.text} />
                  : <div style={{ color:'#F5F0E8', fontSize:'14px', lineHeight:'1.75', whiteSpace:'pre-wrap' }}>{msg.text}</div>
                }
              </div>
              {msg.sources && msg.sources.length > 0 && (
                <div style={{ width:'90%', marginTop:'10px' }}>
                  <div style={{ fontSize:'11px', color:'#6A6A5A', letterSpacing:'1px', textTransform:'uppercase', marginBottom:'6px' }}>
                    📚 Sources From Database
                  </div>
                  {msg.sources.map((src, j) => <SourceCard key={j} source={src} />)}
                </div>
              )}
            </div>
          ))}
          {loading && (
            <div style={{ display:'flex', flexDirection:'column', alignItems:'flex-start', gap:'6px' }}>
              <div style={{ fontSize:'11px', color:'#C9A84C', letterSpacing:'1.5px', textTransform:'uppercase', fontFamily:"'JetBrains Mono',monospace" }}>
                ⚖ Building your legal argument...
              </div>
              <TypingIndicator />
            </div>
          )}
          <div ref={bottomRef} />
        </div>

        {/* Suggestions */}
        {messages.length === 1 && (
          <div style={{ padding:'0 20px 12px', display:'flex', gap:'8px', flexWrap:'wrap' }}>
            {suggestions.map((s, i) => (
              <button key={i} className="chip" onClick={() => sendMessage(s)} style={{
                background:'rgba(201,168,76,0.06)', border:'1px solid rgba(201,168,76,0.2)',
                borderRadius:'20px', padding:'6px 14px', color:'#C9A84C',
                fontSize:'12px', cursor:'pointer', fontFamily:'inherit', transition:'all 0.2s'
              }}>
                {s.length > 55 ? s.slice(0,55) + '…' : s}
              </button>
            ))}
          </div>
        )}

        {/* Input */}
        <div style={{ padding:'16px 20px', borderTop:'1px solid rgba(201,168,76,0.12)', background:'#0E1220', display:'flex', gap:'12px', alignItems:'flex-end' }}>
          <div style={{ flex:1, background:'rgba(20,24,38,0.9)', border:'1px solid rgba(201,168,76,0.2)', borderRadius:'12px', padding:'12px 16px' }}>
            <textarea
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={handleKey}
              placeholder="Describe your legal situation in detail — the more you share, the stronger the argument..."
              rows={2}
              disabled={loading}
              style={{ width:'100%', background:'transparent', border:'none', color:'#F5F0E8', fontSize:'14px', lineHeight:'1.6' }}
            />
          </div>
          <button className="send-btn" onClick={() => sendMessage()} disabled={loading || !input.trim()} style={{
            width:'48px', height:'48px', borderRadius:'12px', border:'1px solid rgba(201,168,76,0.4)',
            background:'transparent', color:'#C9A84C', fontSize:'18px', cursor:'pointer',
            display:'flex', alignItems:'center', justifyContent:'center', transition:'all 0.2s', flexShrink:0
          }}>➤</button>
        </div>

        <div style={{ textAlign:'center', padding:'8px', fontSize:'10px', color:'#3A3A2A', background:'#0B0F1A' }}>
          BlackCode provides legal information, not legal advice. Consult a qualified advocate for court proceedings.
        </div>
      </div>
    </div>
  );
}
