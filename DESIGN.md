---
name: YouTube Converter
description: A local MP3/MP4 converter built as a hi-fi component faceplate you operate.
colors:
  desk: "#c9ccd1"
  desk-light: "#dfe1e4"
  plate-hi: "#f3f4f5"
  plate-lo: "#d9dbde"
  engrave: "#383b40"
  engrave-soft: "#555961"
  key-top: "#ffffff"
  key-bot: "#e4e5e8"
  key-down-top: "#eceef0"
  key-down-bot: "#dcdee1"
  key-text: "#1c1e21"
  led-off: "#9a9ea5"
  led-on: "#2f86ff"
  glass: "#060b0d"
  vfd: "#a6e6ff"
  vfd-dim: "rgb(166 230 255 / .62)"
  vfd-ghost: "rgb(166 230 255 / .07)"
  vfd-warn: "#ffbb55"
  desk-dark: "#0c0d0f"
  desk-light-dark: "#1a1c1f"
  plate-hi-dark: "#34363a"
  plate-lo-dark: "#25272a"
  engrave-dark: "#c6c9ce"
  engrave-soft-dark: "#a2a6ad"
  key-top-dark: "#4a4c51"
  key-bot-dark: "#36383c"
  key-down-top-dark: "#3a3c40"
  key-down-bot-dark: "#2f3134"
  key-text-dark: "#eef0f3"
  led-off-dark: "#55585e"
typography:
  numeral-lg:
    fontFamily: "DSEG7 Classic, monospace"
    fontSize: "26px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.04em"
    fontFeature: "tnum"
  numeral:
    fontFamily: "DSEG7 Classic, monospace"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.04em"
    fontFeature: "tnum"
  title:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.3
  input:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
  key:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.06em"
  key-transport:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.16em"
  caption:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
  legend:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.14em"
  vfd-label:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.12em"
  fine:
    fontFamily: "Lato, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  segment: "1px"
  pip: "2px"
  chip: "3px"
  eject: "5px"
  key: "6px"
  well: "9px"
  transport: "10px"
  plate: "14px"
spacing:
  key-gap: "6px"
  tight: "8px"
  sm: "10px"
  md: "12px"
  lg: "14px"
  xl: "16px"
  bank: "18px"
components:
  faceplate:
    backgroundColor: "{colors.plate-hi}"
    textColor: "{colors.engrave}"
    rounded: "{rounded.plate}"
    padding: "18px 22px 22px"
  display-window:
    backgroundColor: "{colors.glass}"
    textColor: "{colors.vfd}"
    rounded: "{rounded.key}"
    padding: "14px 16px 16px"
  key:
    backgroundColor: "{colors.key-top}"
    textColor: "{colors.key-text}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0 14px"
    height: "56px"
  key-latched:
    backgroundColor: "{colors.key-down-top}"
    textColor: "{colors.key-text}"
    rounded: "{rounded.key}"
  key-preset:
    backgroundColor: "{colors.key-top}"
    textColor: "{colors.key-text}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    height: "52px"
  key-well:
    rounded: "{rounded.well}"
    padding: "5px"
  key-transport:
    backgroundColor: "{colors.key-top}"
    textColor: "{colors.key-text}"
    typography: "{typography.key-transport}"
    rounded: "{rounded.transport}"
    height: "150px"
  led-pip:
    backgroundColor: "{colors.led-off}"
    rounded: "{rounded.pip}"
    width: "14px"
    height: "4px"
  led-pip-on:
    backgroundColor: "{colors.led-on}"
    rounded: "{rounded.pip}"
  eject-key:
    textColor: "{colors.vfd}"
    typography: "{typography.vfd-label}"
    rounded: "{rounded.eject}"
    padding: "0 10px"
    height: "30px"
  link-input:
    textColor: "{colors.vfd}"
    typography: "{typography.input}"
  file-tag:
    textColor: "{colors.vfd}"
    typography: "{typography.vfd-label}"
    rounded: "{rounded.chip}"
    padding: "4px 6px"
---

# Design System: YouTube Converter

## Overview

**Creative North Star: "The Component on the Rack"**

The converter is a single piece of hi-fi equipment, not a web form. One rack-proportioned faceplate sits centred on a soft desk surface: brushed silver in light appearance, graphite in dark. A recessed black-glass vacuum-fluorescent window glows ice blue and carries everything that changes (the link, the video, the duration and output readout, the level meter, the saved files, errors). Below and beside it are physical keys that latch down with a blue LED pip, grouped into recessed wells, labelled with engraved small-caps legends. Numbers that count are seven-segment numerals with ghost segments showing through the glass.

The style is minimal skeuomorphism: crisp, high-contrast, physically legible, with every raised object edged by a dark 1px ring and a hard 1px top highlight. It is dense and quick, because it serves short bursts of use: paste, latch, press, reveal. Ornament never costs a step. Light in this world is literal: the VFD text, the meter segments and the LEDs emit a glow because they are emitters; nothing else does.

Confirmed rejections from the user: mushy, low-contrast neumorphism (same-colour soft dual shadows, edges that dissolve into the surface), and anything that makes the task slower than a plain form.

**Key Characteristics:**
- One faceplate, one glass window, one key bank; no cards, no page chrome.
- Two materials (anodised plate, black glass) and two emitters (ice-blue VFD, blue LED); amber only for warnings in the glass.
- Keys latch: travel down 2px, darken, go inset, light their LED.
- Engraved 11px uppercase legends on metal; seven-segment numerals behind glass.
- Light and dark swap the plate and keys only; glass, VFD and LEDs are identical in both.
- Bundled Lato, DSEG7 Classic and Lucide-style stroke icons; no external runtime.

## Colors

A near-monochrome metal palette with two lit accents: ice-blue phosphor inside the glass, saturated blue LED on the plate.

### Primary
- **Indicator Blue** (`led-on`): the LED pip on every latched key, the power LED, the transport knob's LED ring and icon, keyboard focus rings and text selection. It is the only saturated colour on the metal. Always carries its glow (`--led-glow`, 65% of itself) and a radial hot spot (`#cfe3ff` at 40%/35%).

### Secondary
- **Ice Phosphor** (`vfd`): all text and segments inside the display glass: link input, caret, video title, readouts, lit meter segments, file names, eject and clear keys. Its derived steps do the hierarchy: **Dim Phosphor** (`vfd-dim`, 62%) for labels, placeholders and secondary meta; **Ghost Segment** (`vfd-ghost`, 7%) for unlit seven-segment digits and unlit meter cells. Inside the glass, hairlines run at 12–18% of Ice Phosphor, key outlines at 30–35%, and fills at 6–14%.

### Tertiary
- **Warning Amber** (`vfd-warn`): the only second emitter colour. Used for invalid-link status and the error block inside the glass, with its own amber glow. Never on the plate.

### Neutral
- **Desk Grey / Desk Light** (`desk`, `desk-light`; dark `desk-dark`, `desk-light-dark`): the page background, a radial falloff from the top centre. It is the surface the unit sits on, not a material of the unit.
- **Plate Highlight / Plate Low** (`plate-hi`, `plate-lo`; dark variants): the faceplate's vertical gradient under the brushing and sheen.
- **Engraving** (`engrave`; dark `engrave-dark`): legends, brand line, footer text on metal.
- **Soft Engraving** (`engrave-soft`; dark `engrave-soft-dark`): secondary engraved text (model line, destination note, quality hint).
- **Key White / Key Shadowside** (`key-top`, `key-bot`): resting key face gradient. **Key Down** (`key-down-top`, `key-down-bot`) for latched keys. In dark appearance the keys become graphite (`key-top-dark` and kin), not white.
- **Key Legend** (`key-text`; dark `key-text-dark`): text and icons on keys.
- **LED Off** (`led-off`; dark `led-off-dark`): unlit pips, sunk with an inner shadow.
- **Black Glass** (`glass`): the VFD window field, with a pure black inner edge.

### Named Rules
**The Two Emitters Rule.** Only Ice Phosphor (in the glass) and Indicator Blue (on keys and LEDs) are lit colours; Warning Amber replaces Ice Phosphor only to signal a fault. The metal itself is never tinted.

**The Same Glass Rule.** The glass, phosphor, LED and amber values do not change with colour scheme. Dark mode swaps the desk, plate, engraving and keys only, the way a graphite unit still has the same display.

## Typography

**Body Font:** Lato 400/600/700 (with system-ui, sans-serif), bundled
**Numeral Font:** DSEG7 Classic Bold (with monospace), bundled

**Character:** Lato is the stamped, engraved and phosphor text of the unit: compact, bold at small sizes, wide-tracked in uppercase. DSEG7 is reserved for numbers that the machine measures, so a glance separates "what the device reports" from "what is written on it".

### Hierarchy
- **Numeral Large** (DSEG7 700, 26px, 1): the duration readout at rest.
- **Numeral** (DSEG7 700, 22px, 1): percent and ETA during a run. Units ride alongside at 10px, 700, 0.14em, Dim Phosphor.
- **Title** (700, 16px, 1.3): the video title in the glass, two-line clamp, balanced wrap.
- **Input** (600, 15px, 1.3): the pasted link, in phosphor with glow.
- **Body** (400, 14px, 1.4): the base; error messages and file names (600) in the glass. Channel and duration meta sit at 13px Dim Phosphor.
- **Key** (700, 13px, 0.06em): legends on format and preset keys. The transport key uses **Key Transport** (700, 14px, 0.16em, uppercase).
- **Caption** (400, 12px): the quality hint under the bank and the footer note.
- **Legend** (700, 11px, 0.14em, uppercase): engraved group labels on metal. The brand line is the same legend at 12px, 0.2em.
- **VFD Label** (700, 11px, 0.12em, uppercase): labels and status inside the glass (LINK, READY, phase names), eject key text, file tags.
- **Fine** (400, 11px, 1.35): destination note, licence line, saved-file sub-line.

### Named Rules
**The Engraving Rule.** Text on metal is never coloured; it is Engraving or Soft Engraving with a 1px highlight cast directly below (`text-shadow: 0 1px 0 var(--engrave-hi)`, white in light, black in dark), so it reads as cut into the plate.

**The Measured Numbers Rule.** Durations, percentages and times that the device measures are DSEG7 numerals over a ghost layer of all-segments-lit digits (`88:88`, `888`) in Ghost Segment. Blank digit positions use DSEG's blank glyph (`!`), never a space. Prose numbers (kbps, 1080p, file sizes) stay in Lato.

## Layout

One centred faceplate, max 920px wide, on a full-height desk with 40px/16px page padding. Inside the plate: a header row (power LED, brand legend, model line pushed right), then the **deck**, a two-column grid of the display window (fluid) and a 168px transport column, 18px apart, then the **bank**, separated by an engraved rule (dark 1px line with highlight beneath), holding the key groups in a wrapping row with 18px row and 26px column gaps. A bottom block spans the bank, left-aligned: the quality hint, then the engraved destination note ("Saves to Downloads › YouTube Converter › …") beneath it. The MP4 resolution group is hidden entirely while MP4 is off.

Spacing moves in small physical steps: 6px between keys, 8–12px inside the glass, 14–18px between major regions. The glass is a vertical flex stack with 12px gaps; the readout, run block, file list and error each push to the bottom of the glass (`margin-top: auto`) so the lower edge of the display is where results appear.

At 760px and below the deck stacks to one column, the plate padding tightens to 14px, the model line is dropped, the glass loses its 236px minimum height, the transport key becomes a 64px horizontal bar,  and each key well and its keys stretch to full width with keys sharing it equally.

## Elevation & Depth

Depth is physical and stacked: the plate sits on the desk, keys stand on the plate, wells and the glass window are sunk into it. Every level is built from four ingredients: a 1px dark edge ring, a hard 1px top highlight, a short contact shadow, and (for raised objects only) a soft drop. The plate surface itself is a horizontal brushed texture (repeating 1px hairlines at 2.2% alpha) under a diagonal sheen band at 175deg, over the plate-hi to plate-lo gradient.

### Shadow Vocabulary
- **Plate** (`inset 0 1px 0 var(--plate-shine), inset 0 -1px 0 rgb(0 0 0 / .12), 0 0 0 1px var(--plate-edge), 0 2px 3px rgb(0 0 0 / .18), 0 22px 40px -18px rgb(0 0 0 / .45)`): the faceplate only.
- **Key at rest** (`inset 0 1px 0 var(--key-shine), inset 0 -2px 0 rgb(0 0 0 / .06), 0 0 0 1px var(--key-edge), 0 2px 0 rgb(0 0 0 / .22), 0 4px 6px -2px var(--key-drop)`): every key. The 2px unblurred step is the key's side wall, part of the key's body; it belongs to keys only.
- **Key latched** (`inset 0 1px 2px rgb(0 0 0 / .14), 0 0 0 1px var(--key-edge), 0 1px 0 rgb(0 0 0 / .2)`): with `translateY(2px)`.
- **Window bezel** (`inset 0 1px 2px rgb(0 0 0 / .35)` on a dark-to-light gradient ring, 4px wide): the frame the glass is sunk into.
- **Glass** (`inset 0 0 0 1px var(--glass-edge), inset 0 8px 24px rgb(0 0 0 / .8)`) plus a 160deg reflection at 7% white over the whole window.
- **Well** (`inset 0 1px 3px rgb(0 0 0 / .28), 0 1px 0 var(--engrave-hi)` on `--well`): recessed tray behind each key group.
- **LED off** (`inset 0 1px 1px rgb(0 0 0 / .45)`) / **LED on** (`0 0 0 1px rgb(0 40 120 / .35), 0 0 8px 1px var(--led-glow)`).

### Named Rules
**The Emitted Light Rule.** Blurred glow appears only on things that emit light: phosphor text (`0 0 4px` at 35%), lit meter segments (`0 0 6px` at 55%), amber warnings (`0 0 6px` at 35–40%) and lit LEDs (`0 0 8px 1px`). Plate, keys and legends never glow.

**The Crisp Edge Rule.** Every raised or sunk object has a hard 1px edge (dark ring or highlight line). Never build depth from two soft, same-coloured shadows on a same-coloured surface; that is the neumorphism the user rejected.

## Shapes

Machined, gently radiused rectangles; nothing is pill-shaped or circular except LEDs. Radii scale with object size: meter cells 1px, LED bars 2px, thumbnail and file tags 3px, eject key 5px, keys and glass 6px, wells and window bezel 9px, transport key 10px, faceplate 14px. Inner radii are kept tighter than their container so nested parts read as fitted. LED pips are 14×4px bars on keys and an 8px circle for the power LED. Inside the glass, divisions are 1px phosphor hairlines, not boxes.

## Components

### Keys
Tactile, decisive, latching. The core control of the system.
- **Shape:** softly radiused (`rounded.key`), 56px tall (52px inside wells), min 64px wide, column layout with the LED pip above the legend.
- **Rest:** Key White to Key Shadowside gradient, Key Legend text, Key-at-rest shadow stack.
- **Hover:** the top colour extends to 40% of the face, a slight brightening; no lift.
- **Latched / Active:** `aria-pressed` or `aria-checked` true, or `:active`, moves the key down 2px, switches to the Key Down gradient and inset shadow, and lights the LED. Latched state is never a colour fill.
- **Focus:** 2px Indicator Blue outline, 3px offset.
- **Disabled:** 45% opacity, no travel.
- **Motion:** transform and shadow transition at 90ms `steps(2)`, a snap rather than an ease; removed under reduced motion.

### Key Wells (preset groups)
- Format keys (multi-latch, at least one stays on) and preset keys (one per row, radio behaviour with arrow-key roving) sit in recessed wells: `--well` fill, 5px padding, 6px between keys, engraved legend above.
- A group whose format is off dims to 70% and its LEDs go out, but stays pressable; pressing a preset there latches its format too.

### Transport Knob (LED-ring)
- The single big action: a round push-knob (156px dial, 112px compact) centred in the 168px transport column, with the engraved legend "Convert" (reads "Working" while busy) beneath it (beside it on compact).
- **Ring:** 24 LED segments (4×11px, 8px compact) set radially in a recessed circular well around the knob. The ring is both the indicator and the job meter: unlit grey (`led-off` at 60%) with no video; fully lit Indicator Blue with glow when ready; while converting it fills clockwise from 12 o'clock with the whole job's progress (all formats, not just the current one); during start, encode and merge a single lit segment chases round it in 50ms `steps(1)` hops.
- **Knob face:** machined concentric hairlines over a radial key gradient, hard 1px edge, 3px side wall; presses 2px at 90ms `steps(2)`. The download icon in its centre is grey when idle and glowing blue lines when ready or busy.
- **Disabled** until a video is looked up; focus is a 2px ring offset 4px, following the round shape.

### Display Window (signature component)
- A bezel ring (9px radius, 4px) holding the black glass (6px radius), min 236px tall on desktop, with a faint top-left phosphor bloom and a diagonal reflection.
- **Link row:** VFD Label "LINK", borderless phosphor input with glow and phosphor caret, a 28px outlined clear key that appears only when there is text. Separated from the content by a 16% phosphor hairline that brightens to full phosphor on focus; keyboard focus also rings the whole window in Indicator Blue.
- **Status line:** VFD Label in Dim Phosphor; turns Warning Amber with glow on a bad link.
- **Video:** 132px 16:9 thumbnail (104px compact), slightly desaturated and dimmed to sit in the glass, 3px radius with a phosphor hairline; title, meta and licence beside it. Loading shows phosphor-tint bars and a pulsing thumbnail.
- **Readout:** duration in Numeral Large on the left, the latched output summary ("MP3 192 + MP4 1080P") in VFD Label on the right, above a hairline.
- **Run:** phase label, Numeral percent, speed, Numeral ETA, and a 32-cell level meter (12px tall, 3px gaps). Determinate progress lights cells left to right; indeterminate phases sweep a lit cell across at 40ms per cell, `steps(1)`.

### Saved Files List
- Each row: outlined file tag (`currentColor` 1px border, 3px radius), file name (600, ellipsis) over a Fine sub-line, and an **Eject key**: 30px tall, 5px radius, 35% phosphor outline over a 6% phosphor fill (14% on hover), eject icon plus "SHOW IN FINDER" in VFD Label.

### Icons
- Lucide-style 2px stroke icons, bundled as SVG and painted with `currentColor` through a CSS mask, so they take the colour of the key or glass they sit on. Sizes: 13–14px in glass keys, 18px for the error mark, 30px (22px compact) on the transport key.

## Do's and Don'ts

### Do:
- **Do** put every changing value (video, readouts, progress, results, errors) inside the black glass in Ice Phosphor; keep the metal for fixed legends, keys and short engraved notes.
- **Do** show latched state with travel (2px down), the Key Down gradient, an inset shadow and a lit Indicator Blue LED, driven by `aria-pressed` / `aria-checked`.
- **Do** give every raised or sunk object a hard 1px edge and a 1px top highlight, per the Crisp Edge Rule.
- **Do** set measured numbers in DSEG7 over a Ghost Segment layer, with `!` for blank digits.
- **Do** engrave text on metal: 11px 700 uppercase at 0.14em with a 1px highlight beneath.
- **Do** use `steps()` timing for key travel, LED blink and meter sweep, and drop all of it under `prefers-reduced-motion`.
- **Do** keep glass, phosphor and LED values identical across light and dark; swap only desk, plate, engraving and keys.

### Don't:
- **Don't** use soft, same-colour dual shadows or low-contrast raised surfaces; the user rejected mushy neumorphism.
- **Don't** add steps, confirmations or ornament that slow the paste, latch, convert, reveal flow; the user rejected anything slower to use.
- **Don't** put glow on non-emitters (plate, keys, legends, footer); glow is reserved for phosphor, meter cells, amber warnings and LEDs.
- **Don't** introduce a third lit colour or tint the plate; amber stays inside the glass and only for faults.
- **Don't** mark a selected key with a coloured fill or a check icon; the latch and LED are the state.
- **Don't** imitate YouTube's red or logo anywhere on the unit.
- **Don't** load fonts or icons from a CDN; Lato, DSEG7 and the icon set ship with the page.
