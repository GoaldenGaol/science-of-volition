# Unified Theory Diagram – Science of Volition (dim4)

This document shows the unified architecture of the Science of Volition as a **testable scientific framework**. It connects:

- Narrative-data embeddings → 7-D volitional state vector V(t)
- dim4 as the active latent scalar
- Country-level fertility mapping
- Cooperation / collapse thresholds
- Firm-level fatal pivot / collapse risk

Nodes and arrows are intended as **falsifiable relationships**, not metaphors.  
Some are empirically supported; others are predictions that require further testing.

```mermaid
flowchart TD

%% ========= LAYER 0: DATA & EMBEDDINGS =========
subgraph L0["L0 – Narrative Data & Embeddings"]
    D1["Country narratives<br/>(laws, media, history, policy texts)"]
    D2["Firm narratives<br/>(filings, PR, earnings calls, media, blogs)"]
    E["Embedding model<br/>(frozen encoder, 2023)"]
end

D1 --> E
D2 --> E

%% ========= LAYER 1: LATENT STATE VECTOR V(t) =========
subgraph L1["L1 – Volitional State Vector V(t)"]
    V["V(t) = [dim1..dim7]<br/>1950–2023, 187 countries<br/>+ firm-level V_firm(t)"]
    dim4["dim4(t)<br/>Latent semantic–institutional stress scalar"]
end

E --> V
V --> dim4

%% ========= LAYER 2: EMPIRICAL MAPPINGS =========
subgraph L2["L2 – Empirical Mappings"]
    subgraph Ctry["Country-level mappings"]
        Fmap["Fertility mapping (validated on 2023 snapshot)<br/>TFR(t+18) = f(dim4_country(t))<br/>r ≈ -0.82 (2023 cross-section)<br/>R² ≈ 0.67 (linear), 0.85 (quadratic)"]
        Bands["Regime bands in dim4_country (2023)<br/>&lt;=0.70: high TFR (~4.2)<br/>0.70–1.00: mid TFR (~2.0)<br/>&gt;1.00: low TFR (~1.34)"]
        Threshold1["Irreversibility band (hypothesis, partly supported)<br/>dim4 > 1.0 ⇒ irreversible low-fertility band"]
        CoopThresh["Cooperation collapse threshold (simulation-backed)<br/>dim4 > 0.92 ⇒ cooperation dies in &lt;40 rounds<br/>dim4 > 1.0 ⇒ absorbing defection regime"]
    end

    subgraph Firm["Firm-level mappings"]
        FirmMap["Fatal pivot / collapse mapping<br/>P_collapse(5–7yr) = g(dim4_firm(t))<br/>single-variable logistic regression"]
        AUC["User-reported result (Dec 2025)<br/>121 firms, 1985–2024<br/>Out-of-sample ROC–AUC ≈ 0.937"]
        Miss["Meta 2018: high-risk prediction, no collapse yet<br/>⇒ demonstrates probabilistic, not deterministic, mapping"]
    end
end

dim4 --> Ctry
dim4 --> Firm

dim4 --> Fmap
dim4 --> CoopThresh
dim4 --> FirmMap

Fmap --> Bands
Bands --> Threshold1

FirmMap --> AUC
FirmMap --> Miss

%% ========= LAYER 3: SYSTEM-LEVEL INTERPRETATION =========
subgraph L3["L3 – System-level Volitional Dynamics"]
    Xi["Full state Ξ(t) = (P(t), C(t), B(t), X(t), Ω(t), I(t))"]
    Regimes["Regime types<br/>Ξ*_coop (cooperative equilibrium)<br/>Ξ*_vol (volatile)<br/>Ξ*_frag (fragmentation / collapse)"]
    Haz["Hazard functions<br/>h_country(t) = h(dim4_country)<br/>h_firm(t) = h(dim4_firm)"]
    InvA["Invariant A (empirically supported):<br/>dim4 → TFR(t+18) mapping is global, monotone, high-R²"]
    InvB["Invariant B (partly supported):<br/>dim4 > 1.0 behaves as an irreversible low-fertility band<br/>(requires full 1950–2023 panel for final proof)"]
    InvF["Invariant F (candidate):<br/>dim4_firm predicts fatal pivot risk<br/>(AUC ≈ 0.94 on initial dataset; needs independent replication)"]
end

dim4 --> Haz
Haz --> Regimes
Xi --> Regimes

Fmap --> InvA
Threshold1 --> InvB
FirmMap --> InvF
