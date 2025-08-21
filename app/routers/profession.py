from fastapi import APIRouter


router = APIRouter(prefix="/professions", tags=["professions"])


@router.get("/", response_model=list[str])
async def list_professions():
    return [
        "Abogado", "Médico Cirujano", "Paleontólogo",
        "Ingeniero", "Historiador", "Geógrafo",
        "Biólogo", "Filólogo", "Psicólogo",
        "Matemático", "Arquitecto", "Trabajador Social",
        "Profesor", "Periodista", "Botánico",
        "Físico", "Sociólogo", "Farmacólogo",
        "Químico", "Politólogo", "Enfermero",
        "Fonoaudiólogo", "Bibliotecario", "Paramédico",
        "Técnico de Sonido", "Desarrollador Web", "Músico",
        "Filósofo", "Calígrafo", "Traductor",
        "Antropólogo", "Óptico", "Economista",
        "Administrador", "Lingüista", "Radiólogo",
        "Contador", "Psicoanalista", "Kinesiólogo",
        "Veterinario", "Astrónomo", "Meteorólogo",
        "Diseñador Gráfico", "Odontólogo", "Agrónomo",
        "Actuario", "Obstetra"
    ]
