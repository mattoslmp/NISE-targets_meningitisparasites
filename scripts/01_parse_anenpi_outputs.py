#!/usr/bin/env python3
"""Parse AnEnPi outputs and reconstruct human-parasite EC matrices.

Expected input: the original AnEnPi-completo directory from the user package.
The script classifies an EC as an analog candidate when human and parasite share the EC activity and at least one parasite cluster is absent from the human cluster set.
"""
from pathlib import Path
import re, csv, collections

ROOT = Path('AnenPi-completo')
OUT = Path('data/processed')
OUT.mkdir(parents=True, exist_ok=True)
EC_RE = re.compile(r'^(\d+|-)\.(\d+|-)\.(\d+|-)\.(\d+|-)$')

ORGS = {
 'aac':('Angiostrongylus cantonensis genome',ROOT/'angiostrongylus_cantonensi_GENOMA_aac','Drug_targets_angio_canto','listofECaac.20.txt'),
 'anc':('Angiostrongylus cantonensis transcriptome',ROOT/'AngiostrongyLUS_unica_more_60_transcriptoma_anc','Drug_targets.txt','listofECanc.20.txt'),
 'ecg':('Echinococcus granulosus',ROOT/'Echinococus_gran_ecg','Drug_targets.txt','listofECecg.20.txt'),
 'ecm':('Echinococcus multilocularis',ROOT/'Echinococcus_multilocularis_ecm','Drug_targets.txt','listofECecm.20.txt'),
 'tas':('Taenia solium',ROOT/'Taenia_solium_tas','Drug_targets.txt','listofECtas.20.txt'),
 'tox':('Toxocara canis',ROOT/'Toxocara_canis_adult_toc','Drug_targets.txt','listofECtox.20.txt'),
 'onv':('Onchocerca volvulus',ROOT/'onchocerca_volvulus_onv','Drug_targets.txt','listofEConv.20.txt'),
}

def parse_drug_targets(path, tag):
    records=[]; cur=None
    for line in path.read_text(errors='replace').splitlines():
        s=line.strip()
        if EC_RE.match(s): cur=s; continue
        if cur and '|' in line:
            parts=line.split('||')
            nums_h=re.findall(r'\d+', parts[0] if parts else '')
            nums_o=re.findall(r'\d+', parts[1] if len(parts)>1 else '')
            h_cluster=int(nums_h[-2]) if len(nums_h)>=2 else None
            h_count=int(nums_h[-1]) if len(nums_h)>=2 else 0
            o_cluster=int(nums_o[-2]) if len(nums_o)>=2 else None
            o_count=int(nums_o[-1]) if len(nums_o)>=2 else 0
            if h_cluster is not None or o_cluster is not None:
                records.append((cur,h_cluster,h_count,o_cluster,o_count))
    by=collections.defaultdict(lambda:{'h':collections.Counter(),'p':collections.Counter()})
    for ec,hc,hn,pc,pn in records:
        if hc is not None: by[ec]['h'][hc]+=hn
        if pc is not None: by[ec]['p'][pc]+=pn
    rows=[]
    for ec,d in by.items():
        h=set(d['h']); p=set(d['p']); shared=h&p; unique=p-h
        rows.append({'EC':ec,'hsa_clusters':';'.join(map(str,sorted(h))),'org_clusters':';'.join(map(str,sorted(p))),'shared_clusters':';'.join(map(str,sorted(shared))),'parasite_unique_clusters':';'.join(map(str,sorted(unique))),'same_ec_both':bool(h and p),'analog_candidate':bool(h and unique),'homologous_only':bool(h and p and not unique)})
    return rows

summary=[]
for tag,(name,folder,drug,ecfile) in ORGS.items():
    rows=parse_drug_targets(folder/drug, tag)
    with open(OUT/f'{tag}_human_parasite_ec_matrix.csv','w',newline='') as fh:
        fields=list(rows[0].keys()) if rows else ['EC']
        writer=csv.DictWriter(fh, fields); writer.writeheader(); writer.writerows(rows)
    ecs=[x.strip().replace('ec:','') for x in (folder/ecfile).read_text(errors='replace').splitlines() if EC_RE.match(x.strip().replace('ec:',''))]
    summary.append({'tag':tag,'organism':name,'ec_file_n':len(ecs),'drug_ec_entries':len(rows),'same_ec_both':sum(r['same_ec_both'] for r in rows),'analog_candidate_ecs':sum(r['analog_candidate'] for r in rows),'homologous_only_ecs':sum(r['homologous_only'] for r in rows)})

with open(OUT/'dataset_summary.csv','w',newline='') as fh:
    fields=list(summary[0].keys())
    writer=csv.DictWriter(fh, fields); writer.writeheader(); writer.writerows(summary)
print('Parsed', len(summary), 'datasets')
