from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from pygltflib import GLTF2


app = Ursina()

Sky()

# Memuat dan memutar suara
backsound = Audio("backsound/1-05. Minecraft.mp3", autoplay=True, loop=True)
backsound.volume = 2

jump = Audio(
  'backsound/jump.mp3',
  loop = False,
  autoplay = False,
)
jump.volume = 3



# =======================================================================================
# Tembok
tembok_luar = Entity(
    parent=scene,
    scale=0.048,
    position=Vec3(-35, -0.5, -80),
    rotation=Vec3(0, 90, 0),
    model='entity/wall1/wall_with_column.glb',
    collider='box'
)
tembok_luar2 = Entity(
    parent=scene,
    scale=0.048,
    position=Vec3(-31, -0.5, 100),
    rotation=Vec3(0, 0, 0),
    model='entity/wall1/wall_with_column.glb',
    collider='box'
)
# Menggunakan loop untuk membuat tembok
for i in range(-80, 121, 23):
    duplicate(tembok_luar, position=Vec3(-35, -0.5, i))
for i in range(-80, 121, 23):
    duplicate(tembok_luar, position=Vec3(86, -0.5, i))
for i in range(-31, 100, 23):
    duplicate(tembok_luar2, position=Vec3(i, -0.5, 100))
for i in range(-31, 100, 23):
    duplicate(tembok_luar2, position=Vec3(i, -0.5, -100))

 
# =======================================================================================
# Tembok
wall1 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-10, -0.5, 0),
    rotation=Vec3(0, 90, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider='box'
)

wall_lapis1 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-10, -0.5, 0),
    rotation=Vec3(0, 270, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider=None
)

wall2 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-7, -0.5, 53),
    rotation=Vec3(0, 180, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider='box'
)

wall_lapis2 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-7, -0.5, 53),
    rotation=Vec3(0, 0, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider=None
)

wall3 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-7, -0.5, -53),
    rotation=Vec3(0, 180, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider='box'
)

wall_lapis3 = Entity(
    parent=scene,
    scale=0.01,
    position=Vec3(-7, -0.5, -53),
    rotation=Vec3(0, 0, 0),
    model='entity/wall1/PhotoscannedStoneWall01_Final.fbx',
    texture='entity/wall1/PhotoscannedStoneWall01_Final_Photoscanned.png',
    collider=None
)

# Menggunakan loop untuk membuat tembok
for i in range(5, 51, 5):
    duplicate(wall1, position=Vec3(-10, -0.50, i))
    duplicate(wall_lapis1, position=Vec3(-10, -0.50, i))

for i in range(-10, -51, -5):
    duplicate(wall1, position=Vec3(-10, -0.50, i))
    duplicate(wall_lapis1, position=Vec3(-10, -0.50, i))

for i in range(-7, 86, 5):
    duplicate(wall2, position=Vec3(i, -0.50, 53))
    duplicate(wall_lapis2, position=Vec3(i, -0.50, 53))

for i in range(-7, 86, 5):
    duplicate(wall3, position=Vec3(i, -0.50, -53))
    duplicate(wall_lapis3, position=Vec3(i, -0.50, -53))

# =======================================================================================

    robot = FrameAnimation3d(
      'entity/Robot/robot',
      position=(2,0,2),
      fps=15,
      scale=0.015,
      color=color.blue
    )
# =======================================================================================
    
# Membuat entitas univ
university = Entity(
    model="entity/rumah/university.glb",
    scale=0.50,
    position=(70, 0,0 ),
    rotation =(0,90,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
    shader=lit_with_shadows_shader 
)
university1 = Entity(
    model="entity/rumah/administration.glb",
    scale=0.50,
    position=(40, 0,40 ),
    rotation =(0,0,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
    shader=lit_with_shadows_shader 
)

# Membuat entitas masjid
masjid = Entity(
    model="entity/masjid/mosque_cami.glb",
    scale=0.015,
    position=(3, -0.5,-20 ),
    rotation =(0,270,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
    shader=lit_with_shadows_shader 
)
# Membuat entitas parkiran
mobil = Entity(
    model="entity/parkir/cyberpunk_car.glb",
    scale=1,
    position=(10, 0,0 ),
    rotation =(0,0,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
)
lapangan_baket = Entity(
    model="entity/furnitur/basketball_court.glb",
    scale=5,
    position=(70, -0.9,-42 ),
    rotation =(0,0,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
)

kucing = Entity(
    model="entity/furnitur/cats_gajuannie.glb",
    scale=0.1,
    position=(-9, 0.5, 5 ),
    rotation =(0,0,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
    shader=lit_with_shadows_shader 
)
halte = Entity(
    model="entity/furnitur/bus_stop.glb",
    scale=1,
    position=(-11, 0, 10 ),
    rotation =(0,270,0),
    collider=None,  # Collider sesuai dengan bentuk mesh objek
    shader=lit_with_shadows_shader 
)

# Membuat entitas rumah
try:
    rumah_model = Entity(
        model="entity/rumah/Cottage_FREE.obj",  # Ganti dengan nama file model Anda
        texture="entity/rumah/Warna.png",       # Tambahkan tekstur jika diperlukan
        scale=0.8,                   # Mengubah ukuran model rumah
        position=(-28, 0, 0),       # Menempatkan rumah di posisi tertentu dalam dunia
        rotation =(0,270,0),
        collider='mesh'            # Collider sesuai dengan bentuk mesh objek
    )
    print("Model rumah berhasil dimuat.")
except Exception as e:
    print(f"Error loading model: {e}")
    
rumah1_model = Entity(
    model = "entity/rumah/2m_tveiten_gamleskulen_square_5degree.glb",
    scale = 0.02,
    position=(-32, 0,20 ),
    rotation =(0,90,0),
    collider=None
)
# =========================================================================================
# Membuat entitas bus
bus_model = Entity(
    model="entity/bis/School_Bus.obj",
    texture="entity/bis/render2.png",
    scale=0.01,
    position=(-20, 0, 30),
    rotation =(0,90,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)

# Membuat entitas mobil
try:
    car = Entity(
        model="entity/mobil/nissan_gt-r_r35_gt.glb",
        scale=1,
        position=(-18, 0, 20),
        rotation =(0,180,0),
        collider=None,
        shader=lit_with_shadows_shader  # Menggunakan shader yang mendukung pewarnaan
    )
    print("Model mobil berhasil dimuat.")
except Exception as e:
    print(f"Error loading model: {e}")




# Fungsi untuk membuat objek bus bergerak maju secara berulang-ulang
def move_bus():
    bus_speed = 0.05  # Kecepatan pergerakan bus
    while True:
        if bus_model.z <= 100:  # Batasan pergerakan bus
            bus_model.z += bus_speed
        else:
            bus_model.z = -100  # Mengatur posisi awal bus ketika mencapai batasan
        yield

# Fungsi untuk membuat objek mobil bergerak maju secara berulang-ulang
def move_gtr():
    gtr_speed = 0.5  # Kecepatan pergerakan mobil
    while True:
        if car.z >= -100:  # Batasan pergerakan mobil
            car.z -= gtr_speed
        else:
            car.z = 100  # Mengatur posisi awal mobil ketika mencapai batasan
        yield

# =========================================================================================
# Membuat entitas kursi taman
sidewalk = Entity(
    model="entity/jalan/sidewalk.glb",
    scale=1,
    position=(-6, -0.10,50 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
sidewalk = Entity(
    model="entity/jalan/sidewalk.glb",
    scale=1,
    position=(6, -0.10,50 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
sidewalk = Entity(
    model="entity/jalan/sidewalk.glb",
    scale=1,
    position=(18, -0.10,50 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
sidewalk = Entity(
    model="entity/jalan/sidewalk.glb",
    scale=1,
    position=(30, -0.10,50 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
# # Membuat entitas warung
# warung_kanan1 = Entity(
#     model="entity/warung/japanese_restaurant.glb",
#     scale=0.5,
#     position=(-60, 0,-80 ),
#     rotation =(0,180,0),
#     collider=None  # Collider sesuai dengan bentuk mesh objek
# )
# warung_kanan2 = Entity(
#     model="entity/warung/japanese_restaurant.glb",
#     scale=0.5,
#     position=(-50, 0,-80 ),
#     rotation =(0,180,0),
#     collider=None  # Collider sesuai dengan bentuk mesh objek
# )
# warung_kanan3 = Entity(
#     model="entity/warung/japanese_restaurant.glb",
#     scale=0.5,
#     position=(-40, 0,-80 ),
#     rotation =(0,180,0),
#     collider=None  # Collider sesuai dengan bentuk mesh objek
# )
warung_kanan4 = Entity(
    model="entity/warung/japanese_restaurant.glb",
    scale=0.5,
    position=(-28, 0,-80 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_kiri1 = Entity(
    model="entity/warung/japanese_restaurant.glb",
    scale=0.5,
    position=(-10, 0,-80 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_kiri2 = Entity(
    model="entity/warung/japanese_restaurant.glb",
    scale=0.5,
    position=(0, 0,-80 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_kiri3 = Entity(
    model="entity/warung/japanese_restaurant.glb",
    scale=0.5,
    position=(10, 0,-80 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_kiri4 = Entity(
    model="entity/warung/japanese_restaurant.glb",
    scale=0.5,
    position=(20, 0,-80 ),
    rotation =(0,180,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)

warung_tj1 = Entity(
    model="entity/warung/kyoto_cityscene_restaurant.glb",
    scale=0.015,
    position=(-10, 0,80 ),
    rotation =(0,0,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_tj2 = Entity(
    model="entity/warung/kyoto_cityscene_restaurant.glb",
    scale=0.015,
    position=(10, 0,80 ),
    rotation =(0,0,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
warung_tj3 = Entity(
    model="entity/warung/kyoto_cityscene_restaurant.glb",
    scale=0.015,
    position=(30, 0,80 ),
    rotation =(0,0,0),
    collider=None  # Collider sesuai dengan bentuk mesh objek
)
try:
    mesin = Entity(
        model="entity/furnitur/vending_machine.glb",  # Ganti dengan nama file model Anda
        scale=0.070,                   # Mengubah ukuran model rumah
        position=(-9, 0, 10),       # Menempatkan rumah di posisi tertentu dalam dunia
        rotation =(0,90,0),
        collider=None            # Collider sesuai dengan bentuk mesh objek
    )
    print("Model mesin berhasil dimuat.")
except Exception as e:
    print(f"Error loading model: {e}")

# # Membuat entitas lampu
# try:
#     lampu = Entity(
#         model="entity/lamp/lamp lowpoly.FBX",  # Ganti dengan nama file model Anda
#         texture = "entity/lamp/lamp lowpoly_metal_AlbedoTransparency.png",  # Tambahkan tekstur jika diperlukan
#         scale=0.01,                   # Mengubah ukuran model rumah
#         position=(35, 0, 0),       # Menempatkan rumah di posisi tertentu dalam dunia
#         rotation =(0,90,0),
#         collider=None            # Collider sesuai dengan bentuk mesh objek
#     )
#     print("Model lampu berhasil dimuat.")
# except Exception as e:
#     print(f"Error loading model: {e}")
# Membuat entitas kursi
try:
    kursi = Entity(
        model="entity/furnitur/bench.glb",  # Ganti dengan nama file model Anda
        scale=0.40,                   # Mengubah ukuran model rumah
        position=(-8, 0, 25),       # Menempatkan rumah di posisi tertentu dalam dunia
        rotation =(0,270,0),
        collider=None            # Collider sesuai dengan bentuk mesh objek
    )
    print("Model bangku berhasil dimuat.")
except Exception as e:
    print(f"Error loading model: {e}")

# =========================================================================================
# Menambahkan tanah
ground = Entity(
    model='plane',
    texture="tektur/asphalt_road.png",
    scale=(130, 1, 200),
    texture_scale=(130, 200),
    position=(30,0,0),
    collider='box'
)
ground1 = Entity(
    model='plane',
    texture="/tektur/asphalt_road_2.jpg",
    scale=(120, 1, 120),
    texture_scale=(60, 60),
    collider=None,
    position=(40,0.1,0)
)

# =========================================================================================
# Membuat First Person Controller
player = FirstPersonController(
    model="cube",
    speed=5,
    color=color.blue,
    position=(0, 0, 0))
player.collider = 'box'
player.cursor.color = color.white

def update():
    if held_keys['shift']:  # Jika tombol Shift ditekan
        player.speed = 15    # Meningkatkan kecepatan pemain menjadi 10
    else:
        player.speed = 5     # Mengembalikan kecepatan pemain ke nilai default (8)
    next(bus_movement)
    next(car_movement)
    

# =========================================================================================
# Loop untuk membuat jalan
jalan_positions = [80, 50, 20, -10, -40, -55]
for pos in jalan_positions:
    jalan = Entity(
        parent=scene,
        scale=0.01,
        position=Vec3(-20, -1, pos),
        rotation=Vec3(0, 270, 0),
        model='entity/jalan/untitled.fbx',
        texture='entity/jalan/rua com faixada.jpg',
        collider=None
    )
    
    
jalan_positions2 = [-1, 30, 60, 90]
for posisi in jalan_positions2:
    jalan2 = Entity(
        parent=scene,
        scale=0.01,
        position=Vec3(posisi, -1, -60),
        rotation=Vec3(0, 180, 0),
        model='entity/jalan/untitled.fbx',
        texture='entity/jalan/rua com faixada.jpg',
        collider=None
    )
jalan_positions3 = [-1, 30, 60, 90]
for posisi1 in jalan_positions3:
    jalan3 = Entity(
        parent=scene,
        scale=0.01,
        position=Vec3(posisi1, -1, 60),
        rotation=Vec3(0, 180, 0),
        model='entity/jalan/untitled.fbx',
        texture='entity/jalan/rua com faixada.jpg',
        collider=None
    )
    
# =========================================================================================
    # Menambahkan pencahayaan
sun = DirectionalLight(parent=scene, y=5, z=6, shadows=True)
sun.look_at(Vec3(1, 1, 1))

ambient_light = AmbientLight(color=color.rgba(1, 1, 1, 0.1))
# =========================================================================================


# Pengaturan jendela
window.fullscreen = False
window.fps_counter.enabled = True
window.exit_button.visible = True
window.title = 'Animasi 3D Lingkungan Sekitar Kampus'
# Menginisialisasi pergerakan bus dan mobil
bus_movement = move_bus()
car_movement = move_gtr()

def input(key):
 
    if key == 'escape':  # Tutup aplikasi ketika tombol 'esc' ditekan
        application.quit()
        
    if key == 'space':
      jump.play()
    else :
        jump.stop()

# Menjalankan aplikasi
app.run()

