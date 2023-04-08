import {Column, Entity, PrimaryGeneratedColumn} from "typeorm";

@Entity()
export class BusEntity{
    @PrimaryGeneratedColumn()
    id:number;
    @Column({})
    routeId:number;
    @Column()
    passengerAmount:number;
}
