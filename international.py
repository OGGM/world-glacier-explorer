# -*- coding: utf-8 -*-
supported_languages = ['en', 'de', 'fr', 'es', 'cn', 'fa', 'it']


trads = {
    'lang_display': {
        # unicode languages cannot be used as selector
        # we still want to diplay them correctly
        'fa' : 'فارسی',
        'cn' : '汉语',
    },
    'clear_button':
        {
            'en': 'Clear selection',
            'de': 'Auswahl aufheben',
            'fr': 'Annuler la sélection',
            'cn': '清空选区',
            'es': 'Anular la selección',
            'fa': 'پاک کردن انتخاب',
            'it': 'Cancella la selezione'
        },
    'bar_glaciers_selected':
        {
            'en': 'Glaciers selected: {} of {}',
            'de': 'Ausgewählte Gletscher: {} von {}',
            'fr': 'Glaciers sélectionnés: {} de {}',
            'cn': '已选择冰川：\n {}条，共计：{}条',
            'es': 'Glaciares selecionados',
            'fa': '{} یخچال های طبیعی انتخاب شده : {} از',
            'it': 'Ghiacciai selezionati: {} di {}'
        },
    'bar_area':
        {
            'en': 'Area',
            'de': 'Fläche',
            'fr': 'Surface',
            'cn': '面积',
            'es': 'Área',
            'fa': 'مساحت',
            'it': 'Area'
        },
    'bar_volume':
        {
            'en': 'Volume',
            'de': 'Volumen',
            'fr': 'Volume',
            'cn': '体积',
            'es': 'Volumen',
            'fa': 'حجم',
            'it': 'Volume'
        },
    'bar_sealevel_text':
        {
            'en': 'Sea-level equivalent: ',
            'de': 'Beitrag zum Meeresspiegelanstieg:<br>',
            'fr': "Élévation du niveau de la mer:<br>",
            'cn': '对应海平面上升高度: ',
            'es': 'Nivel del mar equivalente',
            'fa': 'معادل از سطح دریا',
            'it': 'Innalzamento del livello del mare:<br>'
        },
    'bar_sealevel_y':
        {
            'en': 'Volume in mm sea-level equivalent',
            'de': 'Beitrag zum Meeresspiegelanstieg in mm',
            'fr': 'Élévation du niveau de la mer en mm',
            'cn': '冰川体积对应海平面上升高度（mm）',
            'es': 'Volumen en mm del nivel medio del mar',
            'fa': '(حجمی معادل از سطح دریا (میلی متر',
            'it': 'Innalzamento del livello del mare in mm'
        },
    'map_plot_x':
        {
            'en': 'Longitude',
            'de': 'Geographische Länge',
            'fr': 'Longitude',
            'cn': '经度',
            'es': 'Longitud',
            'fa': 'طول جغرافیایی',
            'it': 'Longitudine'
        },
    'map_plot_y':
        {
            'en': 'Latitude',
            'de': 'Geographische Breite',
            'fr': 'Latitude',
            'cn': '纬度',
            'es': 'Latitud',
            'fa': 'عرض جغرافیایی',
            'it': 'Latitudine'
        },
    'temp_plot_x':
        {
            'en': 'Annual Temperature at avg. altitude (°C)',
            'de': 'Jahresdurchschnittstemperatur in mittlerer Höhe (°C)',
            'fr': "Temperature annuelle à l'altitude moyenne (°C)",
            'cn': '冰川平均高程处的年平均气温（°C）',
            'es': 'Temperatura anual á altura promedio (°C)',
            'fa': '(میانگین دمای سالانه نسبت به ارتفاع (سانتیگراد',
            'it': "Temperatura media annua all'altitudine media (°C)"
        },
    'trend_plot_x':
        {
            'en': 'Temperature trend 1979-2018 (°C/decade)',
            'de': 'Temperaturtrend 1979-2018 (°C/Dekade)',
            'fr': 'Tendance de température 1979-2018 (°C/décade)',
            'cn': '1979-2018年气温变化率（°C/10年）',
            'es': 'Tendencia de la temperatura 1979-2018 (°C/década)',
            'fa': 'روند تغییرات دما(سانتیگراد، دوره ده ساله) ۱۹۷۹-۲۰۱۸',
            'it': 'Tendenza della temperatura 1979-2018 (°C/decade)'
        },
    'trend_plot_y':
        {
            'en': 'Glacier count',
            'de': 'Gletscher Anzahl',
            'fr': 'Nombre de glaciers',
            'cn': '冰川数目',
            'es': 'Número de glaciares',
            'fa': 'تعداد یخچال های طبیعی',
            'it': 'Numero di ghiacciai'
        },
    'precip_plot_x':
        {
            'en': 'Annual Precipitation (mm/yr)',
            'de': 'Jährlicher Niederschlag (mm/Jahr)',
            'fr': 'Précipitations annuelles (mm/an)',
            'cn': '年降水量（mm/年）',
            'es': 'Precipitación anual (mm/an)',
            'fa': '(بارندگی سالانه (میلی متر در سال',
            'it': 'Precipitazione annua (mm/anno)'
        },
    'elev_plot_x':
        {
            'en': 'Mean elevation of the glacier (m a.s.l.)',
            'de': 'Mittlere Höhe des Gletschers (m ü.M.)',
            'fr': 'Altitude moyenne du glacier (m)',
            'cn': '冰川平均海拔（m a.s.l.）',
            'es': 'Elevación media del Glaciar (m s.n.m.)',
            'fa': '(میانگین ارتفاع یخچال (متر',
            'it': 'Altitudine media del ghiacciaio (s.l.m.)'
        },
    'elev_plot_y':
        {
            'en': 'Latitude',
            'de': 'Geographische Breite',
            'fr': 'Latitude',
            'cn': '纬度',
            'es': 'Latitud',
            'fa': 'عرض جغرافیایی',
            'it': 'Latitudine'
        },
    'instructions':
        {
            'en': 'Choose your region of interest by clicking and dragging '
                  'the mouse in the map or in the other figures.<br><b>Reset '
                  'your selection with the "Clear selection"  button on the '
                  'left</b>.<br>For more information about the app and our '
                  'data sources, visit <a href="http://edu.oggm.org/en/latest/'
                  'explorer.html">edu.oggm.org</a>',
            'de': 'Wähle eine Region aus, indem du mit der Maus in der '
                  'Weltkarte oder in den anderen Graphiken klickst und ziehst. '
                  '<br><b>Setze deine Auswahl mit dem "Auswahl aufheben"-'
                  'Button auf der linken Seite zurück</b>. Für mehr '
                  'Informationen zu der App und den Datenquellen gehe auf '
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">'
                  'edu.oggm.org</a>.',
            'fr': 'Choisis une région en cliquant et sélectionnant un rectangle '
                  'sur la carte ou sur les autres figures. '
                  '<br><b>Annule la sélection avec le bouton sur la gauche</b>. '
                  "Pour plus d'informations sur l'appliquation et son utilisation, "
                  'visite <a href="http://edu.oggm.org/en/latest/explorer.html">'
                  'edu.oggm.org</a>.',
            'cn': '在任意图表中点击鼠标左键并拖拽以选择您感兴趣的区域或范围。'
                  '<br><b>单击左侧“清空选区”按钮以清空您选择的区域</b>.<br>关于本'
                  'app及其所用数据的更多信息，请访问'
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">edu.oggm.org</a>',
            'es': 'Escoge tu región de interés haciendo click y arrastrando '
                  'el mouse sobre el mapa o sobre las otras figuras. '
                  '<br><b> Reínicia tu selección con la opción "Anular '
                  'la selección" ubicada en el botón de la izquierda</b>. Para más '
                  'información sobre la aplicación y nuestra base de datos, '
                  'visita '
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">edu.oggm.org</a>',
            'fa': 'منطقه مورد علاقه خود را با کلید کردن روی نقشه یا نمودارها های دیگرانتخاب کنید '
                  '.<br><b>با کلید سمت چپ (پاک کردن انتخاب) می توانید آن را پاک کنید </b>.<br> '
                  '<a href="http://edu.oggm.org/en/latest/explorer.html">edu.oggm.org</a>'
                  'برای اطلاعات بیشتر در مورد اپلیکیشن و منبع داده ها اینجا رو نگاه کنید ',
            'it': 'Scegli la tua regione di interesse cliccando e trascinando '
                  'il mouse nella mappa o nelle altre figure.<br><b>Ripristina '
                  'la tua selezione con il pulsante "Cancella selezione" sulla '
                  "sinistra</b>. Per maggiori informazioni sull'app e sulle nostre "
                  'fonti di dati, visita <a href="http://edu.oggm.org/en/latest/'
                  'explorer.html">edu.oggm.org</a>'
        },
    'abbreviations':
        {
            'en': 'Abbreviations:<br>'
                  '"asl" (above sea level): total glacier volume that is above sea level.<br>'
                  '"bsl" (below sea level): total glacier volume that is below sea level in the ocean (grounded).',
            'de': 'Abkürzungen:<br>'
                  '"asl" (above sea level): diese Rubrik umfasst das Gletschervolumen, das sich oberhalb des Meeresspiegels befindet. <br>'
                  '"bsl" (below sea level): diese Rubrik umfasst das Gletschervolumen, das sich unterhalb des Meerespiegels befindet, also bis auf den Meeresboden reicht.',
            'fr': 'Abbréviations:<br>'
                  '"asl" (above sea level): volume total de glace se trouvant au dessus du niveau de la mer.<br>'
                  '"bsl" (below sea level): volume total de glace se trouvant en dessous du niveau de la mer.',
            'cn': '"asl" (above sea level): 海平面以上，海平面以上的冰川总体积。<br>'
                  '"bsl" (below sea level): 海平面以下，海洋中海平面以下的冰川总体积。',
            'es': '"asl" (above sea level): volumen total del glaciar ubicado sobre el nivel del mar.<br>'
                  '"bsl" (below sea level): volumen total del glaciar ubicado por debajo del nivel del mar.',
            'fa': '"asl" (above sea level):حجم کل یخچال های بالاتر از سطح دریا <br>'
                  '"bsl" (below sea level):حجم کل یخچال های پایین تر از سطح دریا/اقیانوس ها',
            'it': 'Abbreviazioni:<br>'
                  '"asl" (above sea level): volume totale del ghiacciaio che si trova sopra il livello del mare.<br>'
                  '"bsl" (below sea level): volume totale del ghiacciaio che si trova sotto il livello del mare (incagliato).'
        },

}
