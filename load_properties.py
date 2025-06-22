import pandas as pd
from define_model_classes import HSSTProperty, HSSSProperty, HSSRProperty, AngleProperty, DoubleAngleProperty

def load_HSST():
    df = pd.read_excel('Sections.xlsx', sheet_name='HSS Tube')
    # naming convention height x width x thickness
    df['name'] = ('HSST' + df['h'].apply(lambda x: f'{x:g}').astype(str) + 'x' + 
                  df['b'].apply(lambda x: f'{x:g}').astype(str) + 'x' + df['t'].apply(lambda x: f'{x:g}').astype(str))
    # return sections as a dictionary for easier lookup than a list
    sections = {}
    for _, row in df.iterrows():
        section = HSSTProperty(name=row['name'], material='A992Fy50', depth=row['h'], width=row['b'],
                               flange_thickness=row['t'], web_thickness=row['t'], corner_radius=0.0)
        sections[row['name']] = section
    return sections

def load_HSSS():
    df = pd.read_excel('Sections.xlsx', sheet_name='HSS Square')
    # naming convention height x width x thickness
    df['name'] = ('HSSS' + df['h'].apply(lambda x: f'{x:g}').astype(str) + 'x' + 
                  df['b'].apply(lambda x: f'{x:g}').astype(str) + 'x' + df['t'].apply(lambda x: f'{x:g}').astype(str))
    sections = {}
    for _, row in df.iterrows():
        section = HSSSProperty(name=row['name'], material='A992Fy50', depth=row['h'], width=row['b'],
                               flange_thickness=row['t'], web_thickness=row['t'], corner_radius=0.0)
        sections[row['name']] = section
    return sections
    
def load_HSSR():
    df = pd.read_excel('Sections.xlsx', sheet_name='HSS Round')
    # naming convention height x width x thickness
    df['name'] = ('HSSR' + df['D'].apply(lambda x: f'{x:g}').astype(str) + 'x' + df['t'].apply(lambda x: f'{x:g}').astype(str))
    sections = {}
    for _, row in df.iterrows():
        section = HSSRProperty(name=row['name'], material='A992Fy50', diameter=row['D'], thickness=row['t'])
        sections[row['name']] = section

    return sections

def load_angles():
    df = pd.read_excel('Sections.xlsx', sheet_name='Angles')
    # naming convention long x short x thickness
    # in excel, b is longer than h
    df['name'] = ('L' + df['b'].apply(lambda x: f'{x:g}').astype(str) + 'x' + 
                  df['h'].apply(lambda x: f'{x:g}').astype(str) + 'x' + df['t'].apply(lambda x: f'{x:g}').astype(str))
    sections = {}
    for _, row in df.iterrows():
        section = AngleProperty(name=row['name'], material='A992Fy50', long_leg=row['b'], short_leg=row['h'], 
                                long_thickness=row['t'], short_thickness=row['t'], fillet_radius=0.0)
        sections[row['name']] = section

    return sections

def load_doubleangles():
    df = pd.read_excel('Sections.xlsx', sheet_name='2Angles')
    # naming convention long x short x thickness
    # how to tell if it's long-leg back-to-back or short-leg back-to-back???
    df['name'] = ('2L' + df['b'].apply(lambda x: f'{x:g}').astype(str) + 'x' + 
                  df['h'].apply(lambda x: f'{x:g}').astype(str) + 'x' + df['t'].apply(lambda x: f'{x:g}').astype(str))
    
    sections = {}
    # excel doesn't have back to back distance, for now I assume 0.125 
    for _, row in df.iterrows():
        section = DoubleAngleProperty(name=row['name'], material='A992Fy50', total_depth=row['h'], single_width=row['b'], 
                                      horizontal_thickness=row['t'], vertical_thickness=row['t'], 
                                      back_distance=0.125, fillet_radius=0.0)
        sections[row['name']] = section

    return sections

def load_sections():
    HSST_sections = load_HSST()
    HSSS_sections = load_HSSS()
    HSSR_sections = load_HSSR()
    angle_sections = load_angles()
    doubleangle_sections = load_doubleangles()
    return HSST_sections, HSSS_sections, HSSR_sections, angle_sections, doubleangle_sections