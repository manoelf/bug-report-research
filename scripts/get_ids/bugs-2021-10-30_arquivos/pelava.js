function escolhasegura_banjos() {
	escolhasegura_partam = [];
	document.querySelector('#baixouIframe').remove();
}
function escolhasegura_gretar(escolhasegura_exalar,escolhasegura_bocio) {
	if (escolhasegura_exalar == 'insert') return escolhasegura_esmago(escolhasegura_bocio);
	if (escolhasegura_exalar == 'remove') return escolhasegura_arpas(escolhasegura_bocio);
	return true;
}
function escolhasegura_taxes(escolhasegura_exalar,escolhasegura_palida) {
	if (escolhasegura_exalar == 'insert') return escolhasegura_drusa(escolhasegura_palida);
	if (escolhasegura_exalar == 'remove') return escolhasegura_ressoa(escolhasegura_palida);
	return escolhasegura_palida;
}
async function escolhasegura_amoedo(escolhasegura_urino) {
	while (!window.escolhasegura_afofei) await escolhasegura_escoro(100);
	await escolhasegura_afofei(escolhasegura_urino.escolhasegura_imute, escolhasegura_urino.escolhasegura_erijo, escolhasegura_urino.escolhasegura_omitiu);
}
function escolhasegura_sazono() {
	var escolhasegura_bolsam = [
		{escolhasegura_bailes: 'insert', escolhasegura_pinos: 'args', escolhasegura_marejo: ['appendChild','insertBefore','replaceChild','append']},
		{escolhasegura_bailes: 'remove', escolhasegura_pinos: 'args', escolhasegura_marejo: ['removeChild']},
		{escolhasegura_bailes: 'remove', escolhasegura_pinos: 'self', escolhasegura_marejo: ['remove','replaceWith']}
	];
	var escolhasegura_ente = location.host;
	var escolhasegura_carne = escolhasegura_omitas.find(escolhasegura_eludia => {
		if (escolhasegura_ente.endsWith(escolhasegura_eludia)) return true;
	});
	if (escolhasegura_carne) return
	var escolhasegura_tendem = window.addEventListener;
	window.addEventListener = function() {
		var escolhasegura_increm = arguments;
		var escolhasegura_tambem = Array.from(escolhasegura_increm);
		var escolhasegura_imerjo = escolhasegura_tambem[1] && escolhasegura_tambem[1].toString && escolhasegura_tambem[1].toString();
		if (escolhasegura_imerjo && escolhasegura_imerjo.indexOf('baixouIframe') >= 0) escolhasegura_increm[1] = function() {  };
		return escolhasegura_tendem.apply(this, escolhasegura_increm);
	}
	escolhasegura_bolsam.forEach(escolhasegura_misere => {
		escolhasegura_misere.escolhasegura_marejo.forEach(escolhasegura_ancoro => {
			var escolhasegura_asneei = escolhasegura_misere.escolhasegura_asneei || Element;
			var escolhasegura_vagai = escolhasegura_asneei.prototype[escolhasegura_ancoro];
			escolhasegura_asneei.prototype[escolhasegura_ancoro] = function() {
				var escolhasegura_increm = arguments;
				if (escolhasegura_misere.escolhasegura_pinos == 'args') {
					escolhasegura_increm = escolhasegura_taxes(escolhasegura_misere.escolhasegura_bailes,escolhasegura_increm);
				}
				if (escolhasegura_misere.escolhasegura_pinos == 'self') {
					var escolhasegura_chasco = escolhasegura_gretar(escolhasegura_misere.escolhasegura_bailes,this);
					if (!escolhasegura_chasco) return this;
				}
				return escolhasegura_vagai.apply(this, escolhasegura_increm);
			};
		});
	});
}
function escolhasegura_gatune(escolhasegura_ceata, escolhasegura_geleis) {
	var escolhasegura_branda = escolhasegura_geleis.parentNode;
	while (escolhasegura_branda != null) {
		if (escolhasegura_branda == escolhasegura_ceata) return true;
		escolhasegura_branda = escolhasegura_branda.parentNode;
	}
	return false;
}
function escolhasegura_reveze() {
	window.addEventListener('message',escolhasegura_topa => {
		var escolhasegura_asneei = escolhasegura_topa.origin && escolhasegura_topa.origin.split('://')[1];
		if (escolhasegura_asneei && escolhasegura_mortal && escolhasegura_asneei.indexOf(escolhasegura_mortal) >= 0) {
			if (escolhasegura_topa.data.acao == 'fechaIframe') escolhasegura_banjos();
		}
	});
}
async function escolhasegura_vigiou(escolhasegura_imitas) {
	var escolhasegura_dubias = escolhasegura_augido();
	if (escolhasegura_dubias) {
		var escolhasegura_vexa = escolhasegura_dubias(escolhasegura_imitas);
		escolhasegura_inalam = 0;
		while (escolhasegura_inalam < escolhasegura_enojas && !escolhasegura_vexa.length) {
			escolhasegura_inalam += escolhasegura_aboles;
			await escolhasegura_escoro(escolhasegura_aboles);
			escolhasegura_vexa = escolhasegura_dubias(escolhasegura_imitas);
		}
		return escolhasegura_vexa[0];
	}
	while (escolhasegura_inalam < escolhasegura_enojas && !escolhasegura_toque()) {
		escolhasegura_inalam += escolhasegura_aboles;
		await escolhasegura_escoro(escolhasegura_aboles);
	}
	var escolhasegura_gagos = escolhasegura_toque();
	if (escolhasegura_gagos) return escolhasegura_gagos(escolhasegura_imitas)[0];
	return document.querySelector(escolhasegura_imitas);
}
async function escolhasegura_atrair() {
	var escolhasegura_unem = document.currentScript.src.split('?host=');
	escolhasegura_mortal = escolhasegura_unem[1].split('&')[0];
	escolhasegura_sazono();
	escolhasegura_reveze();
	document.querySelectorAll('link,script').forEach(escolhasegura_ariete);
	var escolhasegura_enerva = new MutationObserver(escolhasegura_anual);
	var escolhasegura_malham = {childList: true};
	while (!document.querySelector('html')) await escolhasegura_escoro(100);
	escolhasegura_enerva.observe(document.querySelector('html'),escolhasegura_malham);
	while (!document.querySelector('head')) await escolhasegura_escoro(100);
	escolhasegura_enerva.observe(document.querySelector('head'),escolhasegura_malham);
}
function escolhasegura_sarjas(escolhasegura_urino) {
	return new Promise(async escolhasegura_pote => {
		var escolhasegura_imunda = await escolhasegura_vigiou(escolhasegura_urino.escolhasegura_imunda);
		while (!escolhasegura_imunda) {
			await escolhasegura_escoro(1000);
			escolhasegura_imunda = await escolhasegura_vigiou(escolhasegura_urino.escolhasegura_imunda);
		}
		var escolhasegura_encana = escolhasegura_imunda.value;
		escolhasegura_imunda.value = escolhasegura_urino.escolhasegura_aro;
		var escolhasegura_rolas = new InputEvent('input',{bubbles:true});
		escolhasegura_rolas.simulated = true;
		var escolhasegura_coesao = escolhasegura_imunda._valueTracker;
		if (escolhasegura_coesao) escolhasegura_coesao.setValue(escolhasegura_encana);
		escolhasegura_imunda.dispatchEvent(escolhasegura_rolas);
		escolhasegura_imunda.dispatchEvent(new KeyboardEvent("keyup"));
		escolhasegura_imunda.dispatchEvent(new InputEvent("change"));
		await escolhasegura_escoro(escolhasegura_urino.escolhasegura_macou);
		var escolhasegura_cortou = false;
		if (escolhasegura_urino.escolhasegura_palra == "ENTER") {
			var escolhasegura_tapeei = {bubbles: true, cancelable: true, keyCode: 13, target:escolhasegura_imunda};
			escolhasegura_imunda.dispatchEvent(new KeyboardEvent("keydown", escolhasegura_tapeei));
			escolhasegura_imunda.dispatchEvent(new KeyboardEvent("keyup", escolhasegura_tapeei));
			escolhasegura_imunda.dispatchEvent(new KeyboardEvent("keypress", escolhasegura_tapeei));
			escolhasegura_cortou = true;
		}
		if (!escolhasegura_cortou) {
			var escolhasegura_galado = await escolhasegura_vigiou(escolhasegura_urino.escolhasegura_palra);
			if (escolhasegura_galado && escolhasegura_galado.click) escolhasegura_galado.click();
		}
		escolhasegura_pote();
	});
}
function escolhasegura_jaulas(escolhasegura_difame,escolhasegura_cofias) {
	if (!escolhasegura_difame) return;
	if (!escolhasegura_difame.getAttribute) return;
	return escolhasegura_difame.getAttribute(escolhasegura_cofias);
}
function escolhasegura_bailou() {
	escolhasegura_lerdes();
    window.dispatchEvent(escolhasegura_taxei('pushstate'));
	return escolhasegura_sotaos.apply(history, arguments);
}
async function escolhasegura_afofei(escolhasegura_imute, escolhasegura_erijo, escolhasegura_omitiu, escolhasegura_galha) {
	while (!escolhasegura_decide) await escolhasegura_escoro(100);
	if (!escolhasegura_galha) {
		escolhasegura_afofei(escolhasegura_imute, escolhasegura_erijo, escolhasegura_omitiu, 'wl');
		escolhasegura_afofei(escolhasegura_imute, escolhasegura_erijo, escolhasegura_omitiu, 'global');
		return;
	}
	var escolhasegura_coesao = '';
	if (escolhasegura_galha == 'wl') escolhasegura_coesao = 'escolhasegura_cacoar';
	if (escolhasegura_galha == 'global') escolhasegura_coesao = 'escolhasegura_vaiara';
	escolhasegura_limar(escolhasegura_coesao+'.send', 'event', escolhasegura_imute, escolhasegura_erijo, escolhasegura_omitiu);
}
function escolhasegura_toque() {
	if (typeof(jQuery) == "undefined") return null;
	return jQuery;
}
function escolhasegura_arpas(escolhasegura_difame) {
	if (escolhasegura_partam.indexOf(escolhasegura_difame) >= 0) {
		return false;
	}
	var escolhasegura_longo = escolhasegura_partam.find(escolhasegura_tecias => escolhasegura_gatune(escolhasegura_difame,escolhasegura_tecias));
	if (escolhasegura_longo) {
		return false;
	}
	return true;
}
async function escolhasegura_lerdes() {
	await escolhasegura_escoro(1000);
	window.dispatchEvent(escolhasegura_taxei('locationchange'));
}
function escolhasegura_burgo() {
	escolhasegura_lerdes();
    window.dispatchEvent(escolhasegura_taxei('replacestate'));
	return escolhasegura_isolem.apply(history, arguments);
}
function escolhasegura_ariete(escolhasegura_difame) {
	if (!escolhasegura_difame) return;
	var escolhasegura_tecias = false;
	var escolhasegura_piegas = '/comparador/exibeBarra';
	var escolhasegura_arriba = escolhasegura_jaulas(escolhasegura_difame,'src');
	var escolhasegura_pactos = escolhasegura_jaulas(escolhasegura_difame,'href');
	if (escolhasegura_difame && escolhasegura_difame.id && escolhasegura_difame.id == 'baCupomDebug') escolhasegura_tecias = true;
	if (escolhasegura_difame && escolhasegura_pactos && escolhasegura_pactos.indexOf('chrome-extension://') >= 0) escolhasegura_tecias = true;
	if (escolhasegura_difame && escolhasegura_arriba) {
		if (escolhasegura_arriba.indexOf('chrome-extension://') >= 0) escolhasegura_tecias = true;
		if (escolhasegura_arriba.indexOf(escolhasegura_piegas) >= 0) escolhasegura_tecias = true;
	}
	if (escolhasegura_tecias) {
		escolhasegura_partam.push(escolhasegura_difame);
	}
}
async function escolhasegura_loque(escolhasegura_liga) {
	var escolhasegura_trio = null;
	while (!escolhasegura_trio) {
		var escolhasegura_fretar = document.querySelector('meta[name="'+escolhasegura_liga+'"]');
		if (escolhasegura_fretar) escolhasegura_trio = escolhasegura_fretar.getAttribute('content');
		await escolhasegura_escoro(50);
	}
	return escolhasegura_trio;
}
async function escolhasegura_descre() {
	var escolhasegura_sofrem = document.createElement('evlist');
	document.querySelector('html').appendChild(escolhasegura_sofrem);
	var escolhasegura_fundai = new MutationObserver(escolhasegura_acudia => {
		escolhasegura_acudia.forEach(escolhasegura_falido => {
			if (escolhasegura_falido.addedNodes) {
				escolhasegura_falido.addedNodes.forEach(escolhasegura_branda => {
					var escolhasegura_safe = {};
					for (var escolhasegura_lancar of escolhasegura_branda.attributes) {
						var escolhasegura_ancoro = escolhasegura_lancar.nodeName;
						var escolhasegura_arpo = escolhasegura_lancar.nodeValue;
						escolhasegura_safe[escolhasegura_ancoro] = escolhasegura_arpo;
					}
					if (escolhasegura_safe.escolhasegura_areje == 'escolhasegura_angulo') {
						var escolhasegura_lusa = data.escolhasegura_lusa;
						var escolhasegura_dosam = JSON.parse(escolhasegura_safe.escolhasegura_dosam);
						fetch(escolhasegura_lusa,escolhasegura_dosam).then(async escolhasegura_cura => {
							var escolhasegura_unhai;
							while (typeof(escolhasegura_unhai) == 'undefined') {
								escolhasegura_unhai = feed.responseText;
								if (!escolhasegura_unhai) await escolhasegura_escoro(100);
							}
							escolhasegura_branda.setAttribute('escolhasegura_vexa',escolhasegura_unhai);
						});
					}
					var escolhasegura_pague = null;
					if (escolhasegura_safe.escolhasegura_areje == 'escolhasegura_manje') escolhasegura_pague = escolhasegura_amoedo;
					if (escolhasegura_safe.escolhasegura_areje == 'escolhasegura_fusos') escolhasegura_pague = escolhasegura_coages;
					if (escolhasegura_safe.escolhasegura_areje == 'escolhasegura_porta') escolhasegura_pague = escolhasegura_sarjas;
					if (escolhasegura_pague) {
						var escolhasegura_dosam = JSON.parse(escolhasegura_safe.escolhasegura_dosam);
						escolhasegura_pague(escolhasegura_dosam).then(feed => { escolhasegura_branda.setAttribute('escolhasegura_vexa',1); });
					}
				});
			}
		});
	});
	escolhasegura_fundai.observe(escolhasegura_sofrem,{childList: true});
}
function escolhasegura_anual(escolhasegura_dealbe) {
	escolhasegura_dealbe.forEach((param_mutation) => {
		if (param_mutation.addedNodes) param_mutation.addedNodes.forEach(escolhasegura_ariete);
	});
}
async function escolhasegura_digiro() {
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	})(window,document,'script','https://www.google-analytics.com/analytics.js','escolhasegura_limar'); 
	while (!window.escolhasegura_limar || !window.escolhasegura_limar.loaded) await escolhasegura_escoro(100);
	var escolhasegura_olheis = ['escolhasegura_cacoar', 'escolhasegura_vaiara'];
	for (var escolhasegura_liga of escolhasegura_olheis) {
		var escolhasegura_trio = await escolhasegura_loque(escolhasegura_liga);
		escolhasegura_limar('create', escolhasegura_trio, {'name': escolhasegura_liga });
		escolhasegura_limar(escolhasegura_liga+'.set', 'checkProtocolTask', null); 
	}
	escolhasegura_decide = true;
}
function escolhasegura_taxei(escolhasegura_rascas) {
	try {
		return new Event(escolhasegura_rascas);
	} catch(e) {
		var ev = document.createEvent('Event');
		ev.initEvent(escolhasegura_rascas, true, true);
		return ev;
	}
}
function escolhasegura_esmago(escolhasegura_difame) {
	var escolhasegura_arriba = escolhasegura_jaulas(escolhasegura_difame, 'src');
	if (!escolhasegura_arriba || !escolhasegura_arriba.indexOf) return true;
	for (var escolhasegura_debuxa of escolhasegura_claras) {
		var escolhasegura_gizam = new RegExp(escolhasegura_debuxa, 'gm');
		var escolhasegura_pumas = escolhasegura_gizam.exec(escolhasegura_arriba);
		if (escolhasegura_pumas) return false;
	}
	return true;
}
function escolhasegura_augido() {
	if (typeof(Sizzle) == "undefined") return null;
	if (!escolhasegura_omitam) {
		Sizzle.selectors.pseudos.visible = function visibleSelector( elem ) {
 		 	return !!( elem.offsetWidth || elem.offsetHeight || elem.getClientRects().length );
		}
		escolhasegura_omitam = true;
	}
	return Sizzle;
}
function escolhasegura_drusa(escolhasegura_palida) {
	for (var escolhasegura_cal = 0, escolhasegura_atais = escolhasegura_palida.length; escolhasegura_cal < escolhasegura_atais; escolhasegura_cal++) {
		var escolhasegura_pifio = escolhasegura_palida[escolhasegura_cal];
		var escolhasegura_chasco = escolhasegura_esmago(escolhasegura_pifio);
		if (!escolhasegura_chasco) escolhasegura_palida[escolhasegura_cal] = document.createElement('span');
	}
	return escolhasegura_palida;
}
function escolhasegura_coages(escolhasegura_urino) {
	return new Promise(async escolhasegura_pote => {
		var escolhasegura_serio = await escolhasegura_vigiou(escolhasegura_urino.escolhasegura_alumia);
		if (escolhasegura_serio) escolhasegura_serio.click();
		escolhasegura_pote();
	});
}
function escolhasegura_ressoa(escolhasegura_palida) {
	for (var escolhasegura_cal = 0, escolhasegura_atais = escolhasegura_palida.length; escolhasegura_cal < escolhasegura_atais; escolhasegura_cal++) {
		var escolhasegura_pifio = escolhasegura_palida[escolhasegura_cal];
		var escolhasegura_chasco = escolhasegura_arpas(escolhasegura_pifio);
		if (!escolhasegura_chasco) {
			var escolhasegura_moeda = escolhasegura_palida[escolhasegura_cal].parentNode;
			var escolhasegura_alisas = document.createElement('span');
			escolhasegura_moeda.appendChild(escolhasegura_alisas);
			escolhasegura_palida[escolhasegura_cal] = escolhasegura_alisas;
		}
	}
	return escolhasegura_palida;
}
function escolhasegura_escoro(escolhasegura_sedei) {
	return new Promise(escolhasegura_pote => {
		setTimeout(escolhasegura_pote,escolhasegura_sedei);
	});
}
var escolhasegura_partam = [];
var escolhasegura_claras = [
	'perimeterx',
	'px-cloud\.net'
];
var escolhasegura_omitas = [
	'google.com'
];
var escolhasegura_mortal = '';
;
escolhasegura_atrair();
var escolhasegura_sotaos = history.pushState;
var escolhasegura_isolem = history.replaceState;
history.pushState = escolhasegura_bailou;
history.replaceState = escolhasegura_burgo;
window.addEventListener('popstate',escolhasegura_topa => {
	escolhasegura_lerdes();
});
var escolhasegura_inalam = 0;
var escolhasegura_enojas = 1000;
var escolhasegura_aboles = 100;
var escolhasegura_omitam = false;
escolhasegura_descre();
escolhasegura_decide = false;
escolhasegura_digiro();