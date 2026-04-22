import os

replacements = {
    'Logo-Vivas.jpg': 'IMG/Logo-Vivas.jpg',
    'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'IMG/_DSC0020-Editar.jpg',
    'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80': 'IMG/_DSC0251-Editar.jpg',
    'VIVAS ABOGADOS | Firma Legal y Contable': 'Vivas abogados | firma legal y contable',
    'Áreas de Práctica': 'Áreas de práctica',
    'Conocer Servicios': 'Conocer servicios',
    'Agendar Cita': 'Agendar cita',
    'Sobre Vivas Abogados': 'Sobre vivas abogados',
    'Controversias Administrativas': 'Controversias administrativas',
    'Controversias Civiles': 'Controversias civiles',
    'Controversias Familiares': 'Controversias familiares',
    'Controversias Mercantiles': 'Controversias mercantiles',
    'Procedimientos Penales': 'Procedimientos penales',
    'Controversias Laborales': 'Controversias laborales',
    'Nuestro Equipo': 'Nuestro equipo',
    'Javier Vivas Fajardo': 'Javier vivas fajardo',
    'Director | Especialista en Derecho Administrativo y Amparo': 'Director | especialista en derecho administrativo y amparo',
    'Mercedes del Carmen Sántiz Gómez': 'Mercedes del carmen sántiz gómez',
    'Coordinadora de Litigio': 'Coordinadora de litigio',
    'Jorge Alberto Pérez Hernández': 'Jorge alberto pérez hernández',
    'Asociado Especialista en Derecho Penal': 'Asociado especialista en derecho penal',
    'Javier Rosel Natarén Sánchez': 'Javier rosel natarén sánchez',
    'Asociado Especialista en Derecho Laboral': 'Asociado especialista en derecho laboral',
    'Luis Alberto Mercham López': 'Luis alberto mercham lópez',
    'Asociado Especialista y Encargado Contable': 'Asociado especialista y encargado contable',
    'Nuestra Ubicación': 'Nuestra ubicación',
    'Despacho Principal': 'Despacho principal',
    'Controversias Civiles / Familiares': 'Controversias civiles / familiares',
    'Contabilidad / Compliance': 'Contabilidad / compliance',
    'Aviso de Privacidad': 'Aviso de privacidad',
    'Enviar Solicitud': 'Enviar solicitud',
    'Mensaje enviado a Vivas Abogados.': 'Mensaje enviado a vivas abogados.',
    'Vivas Abogados: Soluciones jurídicas estratégicas con visión global y ejecución local.': 'Vivas abogados: soluciones jurídicas estratégicas con visión global y ejecución local.',
    'VIVAS ABOGADOS': 'Vivas abogados',
    'Vivas Abogados': 'Vivas abogados',
}

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for k, v in replacements.items():
    html = html.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Cambios aplicados correctamente.')
