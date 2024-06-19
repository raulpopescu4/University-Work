

#ifndef A23OOP_UNDOREDOREPOSITORY_H
#define A23OOP_UNDOREDOREPOSITORY_H
#include "repository.h"

typedef struct {
    Repository *undo;
    Repository *redo;
    int length_undo;
    int length_redo;
    int capacity_undo;
    int capacity_redo;
}UndoRedoRepository;

UndoRedoRepository createUndoRedoRepo(int capacity);
void destroyUndoRedoRepository(UndoRedoRepository *undo_redo_repo);
void addUndoElement(UndoRedoRepository *undo_redo_repo, Repository *repo);
void addRedoElement(UndoRedoRepository *undo_redo_repo, Repository *repo);
void popLastUndo(UndoRedoRepository *undo_redo_repo, Repository *repo);
void popLastRedo(UndoRedoRepository *undo_redo_repo, Repository *repo);
void resizeArrayUndo(UndoRedoRepository *undo_redo_repo);
void resizeArrayRedo(UndoRedoRepository *undo_redo_repo);
#endif //A23OOP_UNDOREDOREPOSITORY_H
