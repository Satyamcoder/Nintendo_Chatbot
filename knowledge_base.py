"""
Nintendo Switch 2 Knowledge Base
Data sourced from official Nintendo announcements and verified tech reports (2025-2026)
"""

SWITCH_2_KNOWLEDGE = """
# NINTENDO SWITCH 2 - OFFICIAL SPECIFICATIONS & INFORMATION

## RELEASE INFORMATION
- **Official Launch Date**: June 5, 2025
- **Retail Price**: $449.99 (USD), ¥49,980 (Japan - Japanese version), ¥69,980 (Japan - Multi-language)
- **Availability**: Currently available worldwide (as of February 2026)

## HARDWARE SPECIFICATIONS

### Display
- **Screen Size**: Larger than original Switch (specific size not officially disclosed)
- **Resolution**: 
  - Handheld: 1920x1080 (1080p)
  - Docked: Up to 3840x2160 (4K) at 60fps
  - Alternative Docked: 1920x1080 or 2560x1440 at up to 120fps
- **Technology**: LCD display
- **Features**: HDR support (both handheld and docked)

### Processor & Graphics
- **CPU**: Custom ARM processor (8 cores total)
  - System Reservation: 2 cores
  - Available to Developers: 6 cores
- **GPU**: NVIDIA Ampere architecture
  - CUDA Cores: 1536 (vs 256 on original Switch)
  - GPU Clocks:
    - Docked Mode: 1007MHz
    - Handheld Mode: 561MHz
    - Maximum: 1.4GHz
  - Performance:
    - Docked: 3.072 TFLOPs
    - Handheld: 1.71 TFLOPs

### Memory
- **Total RAM**: 12GB LPDDR5X (delivered via two 6GB modules)
- **Memory Interface**: 128-bit
- **Memory Bandwidth**:
  - Docked: 102GB/s
  - Handheld: 68GB/s
- **System Reservation**: 3GB
- **Available for Games**: 9GB

### Storage
- **Internal Storage**: 256GB (UFS)
- **Expandable Storage**: Compatible with microSD Express cards up to 2TB
- **Note**: A portion of internal storage is reserved for system use

## FEATURES

### Controllers & Input
- **Joy-Con 2**: Enhanced controllers with mouse sensor technology
- **Pro Controller**: Available separately
- **GameChat Button**: Dedicated button on controller for accessing chat feature

### Audio & Communication
- **Audio**: Clear audio output
- **Microphone**: Monaural microphone built-in
- **GameChat**: Voice chat functionality (has significant impact on system resources)

### Display Features
- **4K Support**: Yes (when docked)
- **HDR**: Supported in both handheld and docked modes
- **VRR (Variable Refresh Rate)**: Supported

### Connectivity
- **Ports**: Enhanced port selection including expandability options
- **Wireless**: Standard wireless connectivity
- **Wired Gaming**: Supported

### Accessibility
- Multiple accessibility features available

## BACKWARD COMPATIBILITY
- **Switch 1 Games**: Full backward compatibility with original Nintendo Switch games
- **Nintendo Online**: GameCube games available for Nintendo Online subscribers
- **Shared Ecosystem**: Shared eShop with original Switch

## CONFIRMED GAMES (2026)

### Major Titles
- Mario Kart World
- Pokémon Champions (2026)
- Final Fantasy VII Rebirth (2026)
- Fire Emblem: Fortune's Weave (2026)
- Professor Layton and The New World of Steam (2026)
- Indiana Jones and the Great Circle (2026)
- Hollow Knight: Silksong - Sea of Sorrow (2026)
- Phasmophobia (2026)

### Enhanced Editions
- Zelda titles (enhanced versions from Switch 1)
- Hollow Knight - Nintendo Switch 2 Edition (2026)
- Lollipop Chainsaw RePOP - Nintendo Switch 2 Edition (2026)
- Lorelei and the Laser Eyes - Nintendo Switch 2 Edition (2026)
- Sayonara Wild Hearts - Nintendo Switch 2 Edition (2026)

### Q1 2026 Releases
- Pastry Panic! (Q1 2026)
- Planet of Lana II: Children of the Leaf (Q1 2026)
- STARBITES (Q1 2026)
- Starsand Island (Q1 2026)

## COMPARISON: SWITCH 2 VS ORIGINAL SWITCH

| Specification | Switch 2 | Original Switch |
|--------------|----------|-----------------|
| CPU Cores (Dev) | 6 cores | 3 cores |
| GPU Architecture | Ampere | Maxwell |
| CUDA Cores | 1536 | 256 |
| GPU Clock (Docked) | 1007MHz | 768MHz |
| GPU Clock (Handheld) | 561MHz | 460MHz |
| Memory | 12GB LPDDR5X | 4GB LPDDR4 |
| Memory Bandwidth (Docked) | 102GB/s | 25.6GB/s |
| Game Memory Available | 9GB | 3.2GB |
| Max Resolution | 4K@60fps | 1080p@60fps |
| Internal Storage | 256GB | 32GB |

## PRICING CONTEXT
- Price is higher than anticipated by many analysts
- Factors: Current inflation, premium platform positioning
- Comparison: PlayStation 5 Pro priced at $699.99
- Regional pricing: US pricing likely factors in tariff impacts
- Positioned as a premium, ambitious platform with wider ecosystem capabilities

## INDUSTRY CONTEXT
- Switch 1 sold over 150 million units
- Smooth transition expected due to backward compatibility
- Subscription-based services and backward compatibility facilitate upgrade cycle
- Target shipments: Over 10 million units in first year (analyst estimates)
"""

# System prompt for hallucination prevention
SYSTEM_PROMPT = """You are a Nintendo Switch 2 expert assistant. Your role is to provide accurate, helpful information about the Nintendo Switch 2 console.

CRITICAL RULES FOR ACCURACY:
1. **Use ONLY the verified knowledge base provided below to answer questions**
2. **Never invent or speculate about specifications, features, or games not listed**
3. **If information is not in the knowledge base, clearly state**: "I don't have verified information about that in my current knowledge base"
4. **Never present assumptions as facts**
5. **For questions outside Nintendo Switch 2 scope**, politely redirect: "I'm specifically designed to help with Nintendo Switch 2 questions. I can help with specs, features, games, pricing, or comparisons."

RESPONSE GUIDELINES:
- Be conversational and friendly while maintaining accuracy
- Provide specific details when available (exact specs, dates, prices)
- Use comparisons with original Switch when relevant
- Format technical specifications clearly
- If a question could have multiple interpretations, ask for clarification

VERIFIED KNOWLEDGE BASE:
{knowledge_base}

Remember: It's better to admit uncertainty than to provide inaccurate information.
"""