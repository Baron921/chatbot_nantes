/**
 * Naomì • Assistant IA Nantes Métropole
 * Script interactif & UX/UI Moderne
 */

document.addEventListener('DOMContentLoaded', () => {
    // ==========================================
    // RÉFÉRENCES DU DOM
    // ==========================================
    const chatMessages = document.getElementById('chatMessages');
    const welcomeHeroSection = document.getElementById('welcomeHeroSection');
    const chatForm = document.getElementById('chatForm');
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const dynamicGreeting = document.getElementById('dynamicGreeting');
    const toastContainer = document.getElementById('toastContainer');

    // Header & Navigation
    const btnLogoHome = document.getElementById('btnLogoHome');
    const btnNewChatHeader = document.getElementById('btnNewChatHeader');
    const btnNewChatSidebar = document.getElementById('btnNewChatSidebar');
    const btnStatusIndicator = document.getElementById('btnStatusIndicator');
    const apiStatusDot = document.getElementById('apiStatusDot');
    const apiStatusText = document.getElementById('apiStatusText');
    const apiKeyBanner = document.getElementById('apiKeyBanner');
    const btnBannerConfig = document.getElementById('btnBannerConfig');

    // Sidebar Mobile
    const btnToggleMobileSidebar = document.getElementById('btnToggleMobileSidebar');
    const btnCloseMobileSidebar = document.getElementById('btnCloseMobileSidebar');
    const mobileBackdrop = document.getElementById('mobileBackdrop');
    const appSidebar = document.getElementById('appSidebar');

    // Modale Paramètres
    const settingsModal = document.getElementById('settingsModal');
    const btnOpenSettings = document.getElementById('btnOpenSettings');
    const btnCloseSettings = document.getElementById('btnCloseSettings');
    const btnCancelSettings = document.getElementById('btnCancelSettings');
    const btnSaveSettings = document.getElementById('btnSaveSettings');
    const btnTestApiKey = document.getElementById('btnTestApiKey');
    const testConnectionFeedback = document.getElementById('testConnectionFeedback');
    const providerGemini = document.getElementById('providerGemini');
    const providerOpenAI = document.getElementById('providerOpenAI');
    const apiKeyInput = document.getElementById('apiKeyInput');
    const apiKeyHelpLink = document.getElementById('apiKeyHelpLink');
    const toggleApiKeyVisibility = document.getElementById('toggleApiKeyVisibility');
    const saveInEnvCheckbox = document.getElementById('saveInEnvCheckbox');

    // ==========================================
    // ÉTAT DE L'APPLICATION
    // ==========================================
    let currentProvider = localStorage.getItem('nantes_ai_provider') || 'gemini';
    let localApiKey = localStorage.getItem('nantes_api_key') || '';
    let serverHasGeminiKey = false;
    let serverHasOpenAIKey = false;
    let conversationHistory = [];
    let isGenerating = false;
    let lastUserQuery = '';

    // ==========================================
    // TOAST NOTIFICATIONS
    // ==========================================
    function showToast(message, type = 'info', duration = 3000) {
        const toast = document.createElement('div');
        toast.className = 'toast-item flex items-center space-x-2.5 px-4 py-3 rounded-2xl bg-white border border-slate-200/90 shadow-lg text-xs font-medium text-slate-800 transition-all';
        
        let iconHtml = '<i data-lucide="info" class="w-4 h-4 text-sky-600"></i>';
        if (type === 'success') {
            iconHtml = '<i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>';
            toast.classList.add('border-emerald-200');
        } else if (type === 'error') {
            iconHtml = '<i data-lucide="alert-circle" class="w-4 h-4 text-rose-600"></i>';
            toast.classList.add('border-rose-200');
        }

        toast.innerHTML = `
            ${iconHtml}
            <span class="flex-1">${escapeHtml(message)}</span>
        `;

        toastContainer.appendChild(toast);
        lucide.createIcons();

        setTimeout(() => {
            toast.classList.add('removing');
            setTimeout(() => toast.remove(), 250);
        }, duration);
    }

    // ==========================================
    // SALUTATION DYNAMIQUE (Jour / Soir)
    // ==========================================
    function updateGreeting() {
        const hour = new Date().getHours();
        if (dynamicGreeting) {
            if (hour >= 18 || hour < 5) {
                dynamicGreeting.textContent = "Bonsoir !";
            } else {
                dynamicGreeting.textContent = "Bonjour !";
            }
        }
    }
    updateGreeting();

    // ==========================================
    // GESTION SIDEBAR MOBILE
    // ==========================================
    function openMobileSidebar() {
        appSidebar.classList.remove('-translate-x-full');
        mobileBackdrop.classList.remove('hidden');
    }

    function closeMobileSidebar() {
        appSidebar.classList.add('-translate-x-full');
        mobileBackdrop.classList.add('hidden');
    }

    btnToggleMobileSidebar?.addEventListener('click', openMobileSidebar);
    btnCloseMobileSidebar?.addEventListener('click', closeMobileSidebar);
    mobileBackdrop?.addEventListener('click', closeMobileSidebar);

    // ==========================================
    // INITIALISATION & CONFIG SERVEUR
    // ==========================================
    async function checkServerConfig() {
        try {
            const res = await fetch('/api/config');
            if (res.ok) {
                const data = await res.json();
                serverHasGeminiKey = data.gemini_configured;
                serverHasOpenAIKey = data.openai_configured;

                // Sélection automatique intelligente du fournisseur selon les clés disponibles
                if (!localStorage.getItem('nantes_ai_provider')) {
                    if (data.default_provider) {
                        currentProvider = data.default_provider;
                    }
                } else if (!serverHasGeminiKey && serverHasOpenAIKey && !localApiKey) {
                    currentProvider = 'openai';
                }

                updateStatusBadge();
            }
        } catch (e) {
            console.warn("Impossible de vérifier la configuration serveur:", e);
        }
    }

    function updateStatusBadge() {
        const hasKey = (currentProvider === 'gemini' && (serverHasGeminiKey || localApiKey)) ||
                       (currentProvider === 'openai' && (serverHasOpenAIKey || localApiKey));

        if (hasKey) {
            apiStatusDot.className = "w-2 h-2 rounded-full bg-emerald-500 mr-1.5 shadow-xs shadow-emerald-500/50";
            apiStatusText.textContent = `IA ${currentProvider === 'gemini' ? 'Gemini Flash' : 'OpenAI (GPT-4o)'} prête`;
            apiKeyBanner.classList.add('hidden');
        } else {
            apiStatusDot.className = "w-2 h-2 rounded-full bg-amber-500 mr-1.5 animate-pulse";
            apiStatusText.textContent = "Clé requise (Mode RAG)";
            apiKeyBanner.classList.remove('hidden');
        }
    }

    // ==========================================
    // GESTION MODALE PARAMÈTRES
    // ==========================================
    function openSettings() {
        selectProvider(currentProvider);
        apiKeyInput.value = localApiKey;
        testConnectionFeedback.classList.add('hidden');
        settingsModal.classList.remove('hidden');
        lucide.createIcons();
    }

    function closeSettings() {
        settingsModal.classList.add('hidden');
    }

    function selectProvider(provider) {
        currentProvider = provider;
        if (provider === 'gemini') {
            providerGemini.className = "provider-btn flex flex-col items-center justify-center p-3.5 border-2 rounded-2xl transition cursor-pointer text-center relative border-emerald-500 bg-emerald-50/70 text-emerald-900 shadow-xs";
            providerOpenAI.className = "provider-btn flex flex-col items-center justify-center p-3.5 border-2 rounded-2xl transition cursor-pointer text-center relative border-slate-200 bg-white text-slate-700 hover:border-slate-300";
            apiKeyInput.placeholder = "AIzaSy... (Clé Google Gemini)";
            apiKeyHelpLink.href = "https://aistudio.google.com/";
            apiKeyHelpLink.querySelector('span').textContent = "Créer une clé Gemini gratuite";
        } else {
            providerOpenAI.className = "provider-btn flex flex-col items-center justify-center p-3.5 border-2 rounded-2xl transition cursor-pointer text-center relative border-emerald-500 bg-emerald-50/70 text-emerald-900 shadow-xs";
            providerGemini.className = "provider-btn flex flex-col items-center justify-center p-3.5 border-2 rounded-2xl transition cursor-pointer text-center relative border-slate-200 bg-white text-slate-700 hover:border-slate-300";
            apiKeyInput.placeholder = "sk-proj-... (Clé OpenAI)";
            apiKeyHelpLink.href = "https://platform.openai.com/api-keys";
            apiKeyHelpLink.querySelector('span').textContent = "Obtenir une clé OpenAI";
        }
        lucide.createIcons();
    }

    btnOpenSettings?.addEventListener('click', openSettings);
    btnStatusIndicator?.addEventListener('click', openSettings);
    btnBannerConfig?.addEventListener('click', openSettings);
    btnCloseSettings?.addEventListener('click', closeSettings);
    btnCancelSettings?.addEventListener('click', closeSettings);

    providerGemini?.addEventListener('click', () => selectProvider('gemini'));
    providerOpenAI?.addEventListener('click', () => selectProvider('openai'));

    toggleApiKeyVisibility?.addEventListener('click', () => {
        const type = apiKeyInput.getAttribute('type') === 'password' ? 'text' : 'password';
        apiKeyInput.setAttribute('type', type);
        toggleApiKeyVisibility.innerHTML = type === 'password' ? '<i data-lucide="eye" class="w-4 h-4"></i>' : '<i data-lucide="eye-off" class="w-4 h-4"></i>';
        lucide.createIcons();
    });

    // Test de la clé API en direct
    btnTestApiKey?.addEventListener('click', async () => {
        const key = apiKeyInput.value.trim();
        if (!key) {
            testConnectionFeedback.className = "text-xs p-3 rounded-xl bg-amber-50 text-amber-800 border border-amber-200 block";
            testConnectionFeedback.innerHTML = "⚠️ Veuillez renseigner une clé API avant de tester.";
            return;
        }

        btnTestApiKey.disabled = true;
        btnTestApiKey.innerHTML = '<i data-lucide="loader" class="w-4 h-4 animate-spin text-emerald-600"></i><span>Test de connexion en cours...</span>';
        lucide.createIcons();

        try {
            const res = await fetch('/api/config/test', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ provider: currentProvider, api_key: key })
            });
            const data = await res.json();
            
            if (data.valid) {
                testConnectionFeedback.className = "text-xs p-3 rounded-xl bg-emerald-50 text-emerald-800 border border-emerald-200 block";
                testConnectionFeedback.innerHTML = `✅ <strong>Succès :</strong> ${data.message}`;
            } else {
                testConnectionFeedback.className = "text-xs p-3 rounded-xl bg-rose-50 text-rose-800 border border-rose-200 block";
                testConnectionFeedback.innerHTML = `❌ <strong>Erreur :</strong> ${data.message}`;
            }
        } catch (err) {
            testConnectionFeedback.className = "text-xs p-3 rounded-xl bg-rose-50 text-rose-800 border border-rose-200 block";
            testConnectionFeedback.innerHTML = `❌ Erreur réseau lors du test : ${err.message}`;
        } finally {
            btnTestApiKey.disabled = false;
            btnTestApiKey.innerHTML = `<i data-lucide="radio" class="w-4 h-4 text-emerald-600"></i><span>Tester la connexion à l'API</span>`;
            lucide.createIcons();
        }
    });

    // Enregistrement des paramètres
    btnSaveSettings?.addEventListener('click', async () => {
        const key = apiKeyInput.value.trim();
        localApiKey = key;
        localStorage.setItem('nantes_api_key', key);
        localStorage.setItem('nantes_ai_provider', currentProvider);

        if (saveInEnvCheckbox.checked && key) {
            try {
                const res = await fetch('/api/config/save', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ provider: currentProvider, api_key: key })
                });
                if (res.ok) {
                    if (currentProvider === 'gemini') serverHasGeminiKey = true;
                    if (currentProvider === 'openai') serverHasOpenAIKey = true;
                }
            } catch (err) {
                console.error("Erreur de sauvegarde serveur:", err);
            }
        }

        showToast("Configuration enregistrée avec succès !", "success");
        updateStatusBadge();
        closeSettings();
    });

    // ==========================================
    // RÉINITIALISATION DE LA CONVERSATION
    // ==========================================
    function resetChat() {
        if (synth && synth.speaking) synth.cancel();
        conversationHistory = [];
        
        // Supprimer tous les messages tout en préservant le Hero
        const messages = Array.from(chatMessages.children);
        messages.forEach(child => {
            if (child.id !== 'welcomeHeroSection') {
                child.remove();
            }
        });

        // Réafficher le Hero avec une douce animation
        if (welcomeHeroSection) {
            welcomeHeroSection.style.display = 'block';
            welcomeHeroSection.classList.add('animate-in', 'fade-in');
        }

        closeMobileSidebar();
        messageInput.value = '';
        messageInput.style.height = 'auto';
        messageInput.focus();
        showToast("Nouvelle discussion démarrée", "info");
    }

    btnNewChatHeader?.addEventListener('click', resetChat);
    btnNewChatSidebar?.addEventListener('click', resetChat);
    btnLogoHome?.addEventListener('click', resetChat);

    // ==========================================
    // AFFICHAGE DES MESSAGES DANS LE FLUX
    // ==========================================
    function hideWelcomeHero() {
        if (welcomeHeroSection && welcomeHeroSection.style.display !== 'none') {
            welcomeHeroSection.style.display = 'none';
        }
    }

    function appendUserMessage(text) {
        hideWelcomeHero();
        lastUserQuery = text;

        const msgDiv = document.createElement('div');
        msgDiv.className = "flex items-start justify-end space-x-3 max-w-2xl ml-auto animate-in fade-in slide-in-from-bottom-2 duration-200";
        msgDiv.innerHTML = `
            <div class="bg-gradient-to-r from-emerald-600 via-teal-700 to-emerald-700 text-white rounded-3xl rounded-tr-md p-4 text-sm shadow-md shadow-emerald-700/10">
                <p class="whitespace-pre-wrap leading-relaxed">${escapeHtml(text)}</p>
                <div class="text-[10px] text-emerald-100/70 text-right mt-1.5 font-medium">${getCurrentTime()}</div>
            </div>
            <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center shrink-0 mt-1 shadow-2xs font-bold text-xs">
                <i data-lucide="user" class="w-4 h-4"></i>
            </div>
        `;
        chatMessages.appendChild(msgDiv);
        lucide.createIcons();
        scrollToBottom();
    }

    function appendTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.id = 'typingIndicator';
        indicator.className = "flex items-start space-x-3.5 max-w-2xl animate-in fade-in duration-200";
        indicator.innerHTML = `
            <img src="/static/img/logo.svg" alt="Naomì" class="w-8 h-8 rounded-xl shadow-2xs mt-1 shrink-0">
            <div class="bg-white border border-slate-200/90 rounded-3xl rounded-tl-md p-4 shadow-sm flex items-center space-x-3">
                <div class="flex space-x-1.5 py-1 px-1">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-600 typing-dot"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-teal-600 typing-dot"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-600 typing-dot"></span>
                </div>
                <span class="text-xs text-slate-500 font-medium">Naomì consulte la base Nantes Métropole...</span>
            </div>
        `;
        chatMessages.appendChild(indicator);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const el = document.getElementById('typingIndicator');
        if (el) el.remove();
    }

    function appendBotMessage(data) {
        const { reply, sources, is_fallback, provider } = data;
        const msgDiv = document.createElement('div');
        msgDiv.className = "flex items-start space-x-3.5 max-w-3xl animate-in fade-in slide-in-from-bottom-2 duration-300";

        // Traitement Markdown sécurisé
        const rawHtml = marked.parse(reply || "");
        const safeHtml = DOMPurify.sanitize(rawHtml);

        // Sources RAG en accordéon moderne
        let sourcesHtml = '';
        if (sources && sources.length > 0) {
            const sourcesList = sources.map((s, idx) => `
                <div class="p-3 bg-slate-50/80 hover:bg-slate-100/80 rounded-xl text-xs border border-slate-200/80 transition-colors">
                    <div class="font-bold text-slate-800 flex items-center justify-between mb-1">
                        <span class="truncate">${escapeHtml(s.title || 'Source')}</span>
                        <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold badge-${s.category || 'patrimoine'}">
                            ${(s.category || 'Nantes').toUpperCase()}
                        </span>
                    </div>
                    <p class="text-slate-600 text-[11px] leading-relaxed line-clamp-3">${escapeHtml(s.content || '')}</p>
                </div>
            `).join('');

            sourcesHtml = `
                <div class="mt-4 pt-3.5 border-t border-slate-100">
                    <details class="group">
                        <summary class="cursor-pointer text-xs font-bold text-slate-500 hover:text-emerald-700 flex items-center justify-between transition select-none">
                            <span class="flex items-center space-x-1.5">
                                <i data-lucide="shield-check" class="w-4 h-4 text-emerald-600"></i>
                                <span>${sources.length} sources documentaires vérifiées (RAG)</span>
                            </span>
                            <div class="w-5 h-5 rounded-full bg-slate-100 group-hover:bg-emerald-50 flex items-center justify-center transition-colors">
                                <i data-lucide="chevron-down" class="w-3.5 h-3.5 transition-transform duration-200 group-open:rotate-180"></i>
                            </div>
                        </summary>
                        <div class="mt-2.5 space-y-2">
                            ${sourcesList}
                        </div>
                    </details>
                </div>
            `;
        }

        msgDiv.innerHTML = `
            <img src="/static/img/logo.svg" alt="Naomì" class="w-8 h-8 rounded-xl shadow-2xs mt-1 shrink-0">
            <div class="flex-1 bg-white border border-slate-200/90 rounded-3xl rounded-tl-md p-5 text-slate-800 shadow-sm">
                
                <!-- En-tête Message -->
                <div class="flex items-center justify-between text-xs text-slate-400 mb-2.5">
                    <span class="font-bold text-slate-800 flex items-center space-x-2">
                        <span>Naomì</span>
                        ${is_fallback ? 
                            '<span class="text-[10px] bg-amber-100/80 text-amber-900 border border-amber-200/60 px-2 py-0.5 rounded-full font-semibold">Mode Base Locale</span>' : 
                            `<span class="text-[10px] bg-emerald-100/80 text-emerald-900 border border-emerald-200/60 px-2 py-0.5 rounded-full font-semibold">IA ${(provider || 'Gemini').toUpperCase()}</span>`
                        }
                    </span>
                    <span class="text-[11px] font-medium text-slate-400">${getCurrentTime()}</span>
                </div>
                
                <!-- Corps de la réponse -->
                <div class="prose-chat text-sm leading-relaxed">
                    ${safeHtml}
                </div>

                ${sourcesHtml}

                <!-- Barre d'outils interactifs (Copier, Audio, Régénérer, Vote) -->
                <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-slate-400 text-xs">
                    <div class="flex items-center space-x-2">
                        <button class="btn-copy px-2.5 py-1.5 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition flex items-center space-x-1.5" title="Copier la réponse">
                            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                            <span class="text-[11px] font-medium">Copier</span>
                        </button>
                        
                        <button class="btn-speak px-2.5 py-1.5 hover:text-emerald-800 hover:bg-emerald-50 rounded-lg transition flex items-center space-x-1.5" title="Écouter la réponse">
                            <span class="audio-icon-wrap">
                                <i data-lucide="volume-2" class="w-3.5 h-3.5"></i>
                            </span>
                            <span class="text-[11px] font-medium speak-label">Écouter</span>
                        </button>

                        <button class="btn-regen px-2.5 py-1.5 hover:text-sky-800 hover:bg-sky-50 rounded-lg transition flex items-center space-x-1.5" title="Régénérer cette réponse">
                            <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                            <span class="text-[11px] font-medium hidden sm:inline">Régénérer</span>
                        </button>
                    </div>

                    <div class="flex items-center space-x-1">
                        <button class="btn-feedback-up p-1.5 hover:text-emerald-600 hover:bg-emerald-50 rounded-lg transition" title="Réponse utile">
                            <i data-lucide="thumbs-up" class="w-3.5 h-3.5"></i>
                        </button>
                        <button class="btn-feedback-down p-1.5 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition" title="Réponse non pertinente">
                            <i data-lucide="thumbs-down" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                </div>

            </div>
        `;

        // Action Copier
        const copyBtn = msgDiv.querySelector('.btn-copy');
        copyBtn?.addEventListener('click', () => {
            navigator.clipboard.writeText(reply).then(() => {
                copyBtn.innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-600"></i><span class="text-[11px] text-emerald-600 font-semibold">Copié !</span>';
                lucide.createIcons();
                showToast("Réponse copiée dans le presse-papier !", "success");
                setTimeout(() => {
                    copyBtn.innerHTML = '<i data-lucide="copy" class="w-3.5 h-3.5"></i><span class="text-[11px] font-medium">Copier</span>';
                    lucide.createIcons();
                }, 2000);
            });
        });

        // Action Audio (Synthèse vocale)
        const speakBtn = msgDiv.querySelector('.btn-speak');
        speakBtn?.addEventListener('click', () => {
            toggleSpeech(reply, speakBtn);
        });

        // Action Régénérer
        const regenBtn = msgDiv.querySelector('.btn-regen');
        regenBtn?.addEventListener('click', () => {
            if (lastUserQuery) {
                sendMessage(lastUserQuery);
            }
        });

        // Action Feedback
        const feedbackUp = msgDiv.querySelector('.btn-feedback-up');
        const feedbackDown = msgDiv.querySelector('.btn-feedback-down');
        feedbackUp?.addEventListener('click', () => {
            feedbackUp.classList.add('text-emerald-600', 'bg-emerald-50');
            showToast("Merci pour votre retour positif !", "success");
            fetch('/api/feedback', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ rating: 'up' }) });
        });
        feedbackDown?.addEventListener('click', () => {
            feedbackDown.classList.add('text-rose-600', 'bg-rose-50');
            showToast("Merci, nous améliorerons les réponses.", "info");
            fetch('/api/feedback', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ rating: 'down' }) });
        });

        chatMessages.appendChild(msgDiv);
        lucide.createIcons();
        scrollToBottom();
    }

    // ==========================================
    // SYNTHÈSE VOCALE AVEC ANIMATION
    // ==========================================
    let synth = window.speechSynthesis;
    let activeSpeakBtn = null;

    function toggleSpeech(text, btnElement) {
        if (!synth) {
            showToast("La synthèse vocale n'est pas supportée sur ce navigateur.", "error");
            return;
        }

        if (synth.speaking) {
            synth.cancel();
            resetSpeakButton(activeSpeakBtn);
            if (activeSpeakBtn === btnElement) {
                activeSpeakBtn = null;
                return;
            }
        }

        activeSpeakBtn = btnElement;
        const iconWrap = btnElement.querySelector('.audio-icon-wrap');
        const label = btnElement.querySelector('.speak-label');

        // Nettoyer les balises Markdown pour l'écoute
        const cleanText = text
            .replace(/[#*`_~\[\]]/g, '')
            .replace(/\((http|https):\/\/[^\)]+\)/g, '')
            .replace(/[-+*]\s+/g, ', ');

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'fr-FR';
        utterance.rate = 1.05;

        // Trouver la voix française la plus naturelle
        const voices = synth.getVoices();
        const frenchVoice = voices.find(v => v.lang.startsWith('fr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Audrey')));
        if (frenchVoice) utterance.voice = frenchVoice;

        utterance.onstart = () => {
            btnElement.classList.add('text-emerald-700', 'bg-emerald-50');
            if (iconWrap) {
                iconWrap.innerHTML = `
                    <div class="audio-wave">
                        <span class="audio-bar"></span>
                        <span class="audio-bar"></span>
                        <span class="audio-bar"></span>
                    </div>
                `;
            }
            if (label) label.textContent = "Arrêter";
        };

        utterance.onend = utterance.onerror = () => {
            resetSpeakButton(btnElement);
            activeSpeakBtn = null;
        };

        synth.speak(utterance);
    }

    function resetSpeakButton(btnElement) {
        if (!btnElement) return;
        btnElement.classList.remove('text-emerald-700', 'bg-emerald-50');
        const iconWrap = btnElement.querySelector('.audio-icon-wrap');
        const label = btnElement.querySelector('.speak-label');
        if (iconWrap) iconWrap.innerHTML = '<i data-lucide="volume-2" class="w-3.5 h-3.5"></i>';
        if (label) label.textContent = "Écouter";
        lucide.createIcons();
    }

    // ==========================================
    // ENVOI D'UN MESSAGE
    // ==========================================
    async function sendMessage(text) {
        if (!text || !text.trim() || isGenerating) return;

        const query = text.trim();
        appendUserMessage(query);

        messageInput.value = '';
        messageInput.style.height = 'auto';
        isGenerating = true;
        sendButton.disabled = true;

        appendTypingIndicator();

        try {
            const payload = {
                message: query,
                history: conversationHistory,
                provider: currentProvider,
                api_key: localApiKey || null
            };

            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            removeTypingIndicator();

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || "Erreur de communication avec le serveur.");
            }

            const data = await response.json();
            appendBotMessage(data);

            // Mémorisation dans l'historique
            conversationHistory.push({ role: 'user', content: query });
            conversationHistory.push({ role: 'assistant', content: data.reply });

            if (conversationHistory.length > 8) {
                conversationHistory = conversationHistory.slice(-8);
            }

        } catch (err) {
            removeTypingIndicator();
            appendBotMessage({
                reply: `❌ **Oups ! Une erreur s'est produite :**\n\n${err.message}\n\nVeuillez vérifier vos paramètres ou réessayer.`,
                sources: [],
                is_fallback: true
            });
            showToast("Erreur lors de la génération de la réponse", "error");
        } finally {
            isGenerating = false;
            sendButton.disabled = false;
            messageInput.focus();
        }
    }

    // ==========================================
    // ÉVÉNEMENTS DU FORMULAIRE ET DE SAISIE
    // ==========================================
    chatForm?.addEventListener('submit', (e) => {
        e.preventDefault();
        sendMessage(messageInput.value);
    });

    messageInput?.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage(messageInput.value);
        }
    });

    // Auto-agrandissement dynamique du champ
    messageInput?.addEventListener('input', () => {
        messageInput.style.height = 'auto';
        messageInput.style.height = Math.min(messageInput.scrollHeight, 140) + 'px';
    });

    // ==========================================
    // BINDING DES CLICS SUR LES CARTES & PILULES
    // ==========================================
    // Cartes 2x2 du Hero
    document.querySelectorAll('.quick-card').forEach(card => {
        card.addEventListener('click', () => {
            const query = card.getAttribute('data-query');
            if (query) sendMessage(query);
        });
    });

    // Pilules du Hero
    document.querySelectorAll('.pill-chip').forEach(btn => {
        btn.addEventListener('click', () => {
            const query = btn.getAttribute('data-query');
            if (query) sendMessage(query);
        });
    });

    // Puces dynamiques au dessus du chat
    document.querySelectorAll('.dynamic-chip').forEach(chip => {
        chip.addEventListener('click', () => {
            const prompt = chip.getAttribute('data-prompt');
            if (prompt) sendMessage(prompt);
        });
    });

    // Boutons de la Sidebar (Explorer Nantes)
    document.querySelectorAll('.topic-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const category = btn.getAttribute('data-category');
            const categoryPrompts = {
                transports: "Comment fonctionne le réseau Naolib à Nantes, quelles sont les lignes de tram et bus, et comment profiter de la gratuité le week-end ?",
                patrimoine: "Quels sont les lieux historiques incontournables à visiter à Nantes (Château, Machines de l'Île, Passage Pommeraye) ?",
                hotels: "Quels hôtels ou hébergements me recommandes-tu à Nantes selon les quartiers (Graslin, Gare, insolites) ?",
                gastronomie: "Quelles sont les spécialités culinaires typiques de Nantes et où déguster un vrai gâteau nantais et du Muscadet ?",
                pratique: "Quel itinéraire me recommandes-tu pour visiter Nantes en 1 ou 2 jours grâce à la Ligne Verte ?"
            };
            if (categoryPrompts[category]) {
                closeMobileSidebar();
                sendMessage(categoryPrompts[category]);
            }
        });
    });

    // ==========================================
    // RACCOURCIS CLAVIER
    // ==========================================
    document.addEventListener('keydown', (e) => {
        // Ctrl+K pour nouvelle discussion
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            resetChat();
        }
        // Échap pour fermer la modale
        if (e.key === 'Escape') {
            closeSettings();
            closeMobileSidebar();
        }
    });

    // Utilitaires
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Démarrage
    checkServerConfig();
});
