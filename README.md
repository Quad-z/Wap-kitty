🐱 wap-kitty

🇺🇸 English

wap-kitty is a CLI automation utility that dynamically generates and applies harmonious, accessibility-first color schemes for the Kitty terminal based on your current desktop wallpaper using the advanced Material 3 (M3) TonalSpot algorithm.

Unlike traditional palette generators that blindly grab dominant pixels, wap-kitty uses color science and contrast-aware formulas to deliver beautiful, perfectly readable terminal themes every single time.

🚀 How It Works

Wallpaper Detection: Automatically detects your current wallpaper via noctalia integration (by monitoring wallpapers.json) or accepts a direct file path.

Dominant Color Extraction: Quantizes and analyzes the image using material-color-utilities to find the most fitting seed color.

M3 TonalSpot Generation: Uses the seed color to calculate a mathematically precise Material 3 palette, producing Primary, Secondary, Tertiary, Neutral, and Error tonal ranges.

Kitty Theme Mapping: Intelligently maps these tonal vectors to 16 ANSI colors and styles specialized UI elements: background, foreground, cursor, selections, tab bars, and window borders.

Dual-Destination Export: Instantly saves the configuration to two places at once:

~/.cache/wal/colors-kitty.conf (for backward compatibility with the pywal ecosystem)

~/.config/kitty/current-theme.conf (for direct consumption by Kitty)

Live Preview: Prints out the final color scheme right into your terminal with clean, elegant visual color blocks.

📊 How It Differs from pywal

Feature

pywal

wap-kitty (Material 3)

Algorithm

Simple color averaging / K-Means

M3 TonalSpot color science

Palette Tone

Random tones, occasionally muddy or jarring

Harmonious, mathematically bound shades

Accessibility (WCAG)

No contrast enforcement

Strict, built-in contrast and luminance balancing

Kitty Interface Support

Modifies ANSI colors only

Customizes tabs, borders, cursor, and selections

Automation

Requires manual hooks or wrapper scripts

Zero-click automation via native systemd paths

🛠 Seamless Automation "Out of the Box"

The project includes a built-in systemd user unit (wap-kitty.path). It watches for modifications in the noctalia wallpaper configuration file in real-time. The split second your wallpaper changes, the path unit triggers the script, updating your Kitty colors instantly—no user intervention required.

📋 Dependencies

Make sure you have the following installed before running wap-kitty:

Python 3.x

material-color-utilities — for M3 palette generation

Pillow (PIL) — for image processing and analysis

Kitty Terminal

Noctalia — (Optional) required for the automatic wallpaper-tracking mode

💻 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/wap-kitty.git
cd wap-kitty


Install Python dependencies:

pip install pillow material-color-utilities


Configure Kitty:
Add the following line to your ~/.config/kitty/kitty.conf to allow dynamic theme loading:

include current-theme.conf


Enable Automatic Triggers (Systemd):
Copy the provided systemd files to your user configuration directory:

mkdir -p ~/.config/systemd/user/
cp systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path


💡 Usage

Automatic Mode (Default with Noctalia)

If running via systemd or simply launched without arguments, it will read noctalia's config file automatically:

python wap-kitty.py


Manual Mode

Specify a path to any image file to force-generate a theme:

python wap-kitty.py /path/to/your/wallpaper.png


🇷🇺 Русский

wap-kitty — это CLI-утилита автоматизации, которая динамически генерирует и применяет гармоничные цветовые схемы для терминала Kitty на основе текущих обоев рабочего стола, используя продвинутый алгоритм Material 3 (M3) TonalSpot.

В отличие от классических генераторов палитр, которые вслепую берут случайные пиксели, wap-kitty опирается на колористику и стандарты контрастности, обеспечивая красивый и отлично читаемый текст при любой смене обоев.

🚀 Как это работает

Определение обоев: Автоматически определяет текущие обои через интеграцию с noctalia (отслеживая wallpapers.json) либо принимает прямой путь к файлу изображения.

Извлечение доминантного цвета: Проводит квантование и анализ изображения с помощью material-color-utilities для поиска главного цвета.

Применение M3 TonalSpot: На основе главного цвета рассчитывает математически точную палитру Material 3, генерируя тональные диапазоны: Primary, Secondary, Tertiary, Neutral и Error.

Сборка темы для Kitty: Умно маппит полученные оттенки на 16 ANSI-цветов, а также стилизует элементы интерфейса: фон, текст, курсор, выделение, вкладки (tabs) и рамки окон.

Экспорт: Одновременно сохраняет конфигурацию в два места:

~/.cache/wal/colors-kitty.conf (для обратной совместимости с экосистемой pywal)

~/.config/kitty/current-theme.conf (для прямого применения в Kitty)

Визуализация: Выводит финальную цветовую схему прямо в терминал с аккуратными цветными квадратами.

📊 Чем wap-kitty лучше pywal?

Характеристика

pywal

wap-kitty (Material 3)

Алгоритм

Простое усреднение / K-Means

Алгоритм M3 TonalSpot

Палитра

Случайные тона, часто грязные

Гармоничные, связанные оттенки

Доступность (WCAG)

Не контролирует контраст текста

Научно выверенный баланс яркости и контраста

Интерфейс Kitty

Меняет только ANSI-цвета

Кастомизирует табы, рамки, курсор и выделение

Автоматизация

Требует ручного вызова или скриптов

Полный автомат через встроенный systemd.path

🛠 Автоматизация "Из коробки"

В комплект входит встроенный systemd-юнит для пользователя (wap-kitty.path). Он в реальном времени мониторит изменения в конфигурационном файле noctalia. Как только вы меняете обои — юнит мгновенно запускает скрипт, обновляя тему Kitty. Никакого ручного вмешательства.

📋 Зависимости

Перед запуском wap-kitty убедитесь, что у вас установлено следующее:

Python 3.x

material-color-utilities — для расчета M3 палитры

Pillow (PIL) — для обработки и анализа изображений

Терминал Kitty

Noctalia — (Опционально) требуется для автоматического отслеживания обоев

💻 Установка и настройка

Клонируйте репозиторий:

git clone https://github.com/your-username/wap-kitty.git
cd wap-kitty


Установите зависимости Python:

pip install pillow material-color-utilities


Настройте Kitty:
Добавьте следующую строчку в ваш ~/.config/kitty/kitty.conf для динамической загрузки тем:

include current-theme.conf


Включите автоматизацию (Systemd):
Скопируйте файлы юнитов в вашу пользовательскую директорию конфигурации systemd:

mkdir -p ~/.config/systemd/user/
cp systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path


💡 Использование

Автоматический режим (По умолчанию с Noctalia)

Если скрипт запущен через systemd или вручную без аргументов, он сам прочитает конфиг noctalia:

python wap-kitty.py


Ручной режим

Укажите прямой путь к любому изображению для принудительной генерации темы:

python wap-kitty.py /path/to/your/wallpaper.png


🇪🇸 Español

wap-kitty es una utilidad de automatización CLI que genera y aplica dinámicamente esquemas de color armoniosos y enfocados en la accesibilidad para la terminal Kitty, basándose en tu fondo de pantalla actual mediante el algoritmo avanzado Material 3 (M3) TonalSpot.

A diferencia de los generadores de paletas tradicionales que toman píxeles dominantes a ciegas, wap-kitty utiliza la ciencia del color y fórmulas de contraste para ofrecer temas de terminal hermosos y perfectamente legibles en todo momento.

🚀 Cómo Funciona

Detección de Fondo de Pantalla: Detecta automáticamente tu fondo de pantalla actual a través de la integración con noctalia (monitoreando wallpapers.json) o acepta una ruta de archivo directa.

Extracción del Color Dominante: Cuantiza y analiza la imagen usando material-color-utilities para encontrar el color semilla más adecuado.

Generación M3 TonalSpot: Utiliza el color semilla para calcular una paleta Material 3 matemáticamente precisa, produciendo rangos tonales para Primary, Secondary, Tertiary, Neutral y Error.

Mapeo del Tema de Kitty: Mapea de forma inteligente estos vectores tonales a los 16 colores ANSI y personaliza los elementos de la interfaz: fondo, texto, cursor, selecciones, barras de pestañas (tabs) y bordes de ventanas.

Exportación a Doble Destino: Guarda instantáneamente la configuración en dos ubicaciones a la vez:

~/.cache/wal/colors-kitty.conf (para compatibilidad con el ecosistema pywal)

~/.config/kitty/current-theme.conf (para el uso directo de Kitty)

Vista Previa en Vivo: Muestra el esquema de color final directamente en tu terminal con bloques de color visuales limpios y elegantes.

📊 En Qué Se Diferencia de pywal

Característica

pywal

wap-kitty (Material 3)

Algoritmo

Promedio de color simple / K-Means

Ciencia del color M3 TonalSpot

Tono de Paleta

Tonos aleatorios, a veces opacos o discordantes

Tonos armoniosos y vinculados matemáticamente

Accesibilidad (WCAG)

Sin control de contraste

Equilibrio estricto de contraste y luminancia integrado

Soporte de Interfaz Kitty

Modifica solo colores ANSI

Personaliza pestañas, bordes, cursor y selecciones

Automatización

Requiere ganchos manuales o scripts adicionales

Automatización sin clics mediante rutas nativas de systemd

🛠 Automatización Completa de Fábrica

El proyecto incluye una unidad de usuario systemd integrada (wap-kitty.path). Monitorea en tiempo real las modificaciones en el archivo de configuración de fondos de pantalla de noctalia. En el mismo segundo en que cambia tu fondo de pantalla, la unidad activa el script, actualizando los colores de Kitty al instante—sin intervención del usuario.

📋 Dependencias

Asegúrate de tener instalado lo siguiente antes de ejecutar wap-kitty:

Python 3.x

material-color-utilities — para la generación de paletas M3

Pillow (PIL) — para el procesamiento y análisis de imágenes

Terminal Kitty

Noctalia — (Opcional) requerido para el modo de seguimiento automático de fondos de pantalla

💻 Instalación y Configuración

Clonar el repositorio:

git clone https://github.com/your-username/wap-kitty.git
cd wap-kitty


Instalar dependencias de Python:

pip install pillow material-color-utilities


Configurar Kitty:
Añade la siguiente línea a tu ~/.config/kitty/kitty.conf para permitir la carga dinámica de temas:

include current-theme.conf


Activar Automatización (Systemd):
Copia los archivos de systemd proporcionados a tu directorio de configuración de usuario:

mkdir -p ~/.config/systemd/user/
cp systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path


💡 Uso

Modo Automático (Por defecto con Noctalia)

Si se ejecuta a través de systemd o simplemente se inicia sin argumentos, leerá el archivo de configuración de noctalia automáticamente:

python wap-kitty.py


Modo Manual

Especifica la ruta a cualquier archivo de imagen para forzar la generación de un tema:

python wap-kitty.py /ruta/a/tu/fondo_de_pantalla.png


📄 License

This project is licensed under the MIT License.
